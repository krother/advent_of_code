
DROP SCHEMA IF EXISTS day05 CASCADE;
CREATE SCHEMA day05;

CREATE TABLE day05.crates (
  row    SERIAL,
  stacks TEXT
);

CREATE TABLE day05.instructions (
  move     SERIAL,
  sentence TEXT
);

--TODO: dynamic numbers for -A and -B commands; currently hacky but it works (just has to be large enough)
\COPY day05.crates (stacks) FROM PROGRAM 'grep -B100 "^[0-9]*$" input_data.txt | head -n 6';
\COPY day05.instructions (sentence) FROM PROGRAM 'grep -A1000 "^[0-9]*$" input_data.txt | tail -n +2';

WITH RECURSIVE _unnested_crate_rows AS (
  SELECT
    row,
    unnest(REGEXP_SPLIT_TO_ARRAY(stacks, '')) AS crate
  FROM day05.crates
),
_unnested_crates AS (
  SELECT
    *,
   row_number() OVER(PARTITION BY row) AS col
  FROM _unnested_crate_rows
),
unnested_crates AS (
  SELECT
    *
  FROM _unnested_crates
  WHERE mod(col, 4) = 2
	-- positions of the actual letters -> 2, 6, 10, 14, etc.
),
unnested_crates_parsed AS (
  --	 row_num | crate | stack_num 
  --	---------+-------+-----------
  --	       1 |       |         0
  --	       1 | D     |         1
  --	       1 |       |         2
  --	       2 | N     |         0
  --	       2 | C     |         1
  --	       2 |       |         2
  --	       3 | Z     |         0
  --	       3 | M     |         1
  --	       3 | P     |         2
  SELECT
    row AS row_num,
    crate,
    floor(col/4) AS stack_num
  FROM unnested_crates
),
stack_data AS (
  --  stack_num | stack_contents 
  -- -----------+----------------
  --          0 | ZN
  --          1 | MCD
  --          2 | P
  SELECT
    stack_num,
    string_agg(crate, '' ORDER BY row_num DESC) AS stack_contents
  FROM unnested_crates_parsed
  WHERE crate <> ' '
  GROUP BY 1
),
move_vals AS (
  SELECT
    move,
    regexp_match(sentence, 'move (\d+) from (\d+) to (\d+)') AS vals
  FROM day05.instructions
),
moves AS (
  SELECT
    move,
    vals[1]::int AS amount,
    vals[2]::int AS origin,
    vals[3]::int AS destination
  FROM move_vals
), 
initial_stacks AS (
  --the initial configuration of the stacks
  --as the starting point of the recursion
  SELECT
    0 as _round,
    --the advantage of aggregating the stacks into a single array / row is that I can access
    --different stacks within the same move, so that I can easily move contents from the 
    --origin stack to the destination stack (since everything is in the same row / "relation")
    array_agg(stack_contents ORDER BY stack_num) AS stacks_arr
  FROM stack_data
),
stack_round AS ( --The actual recursive CTE
  --initial stacks (non-recursive term)
  SELECT
    _round,
    stacks_arr
  FROM initial_stacks
  UNION ALL
  --subsequent stacks (recursive term)
  SELECT
    stack_round._round + 1 as _round,
    (
      SELECT array_agg(
        CASE 
          WHEN stack_num = origin
            THEN left(stacks_arr[origin], length(stacks_arr[origin]) - amount)
          WHEN stack_num = destination
            THEN stacks_arr[destination] || reverse(right(stacks_arr[origin], amount)) -- append in reverse order!
          ELSE stack
        END
      )
      -- this way is the key to achieving an unnested, enumerated version of the current stacks
      -- WITHOUT needing to use a subquery referencing the recursive term (see comment below)
      FROM unnest(stacks_arr) WITH ORDINALITY AS enum(stack, stack_num)

      -- ---This old way achieves the same thing in theory but doesn't work
      -- ---because a recursive reference to a query cannot appear in a subquery :(
      --	      (
      --	    SELECT
      --		    stack,
      --		    row_number() over() as stack_num
      --	    FROM (SELECT unnest(stacks_arr) stack FROM stack_round)q0
      --	   )q1
	  ) 
    -- and finally, how each recursive term will join on itself to execute each move as a new row
  FROM stack_round
  JOIN moves ON (stack_round._round + 1 = moves.move)
),
top_crates AS (
  SELECT
    right(unnest(stacks_arr), 1) as crates
  FROM (
    SELECT
      stacks_arr
    FROM stack_round
    ORDER BY _round DESC
    LIMIT 1
	)q
)
SELECT
  --For the solution to Part 2, simple remove the reverse function in line 109 :)
  string_agg(crates, '') as "Solution"
FROM top_crates;
