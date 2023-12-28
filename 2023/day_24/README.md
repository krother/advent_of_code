
# Solution of Day 24/2

I solved part 2 of the Day 24 puzzle in a partially manual manner. Here I document how I solved it.

## The Problem

We are looking for a three-dimensional location and displacement vector of the **rock** so that it hits all **hail stones**. All objects move at constant speed and direction and can be described by a **linear equation**:

$\vec{r}(t) = \vec{m}t + \vec{b}$

where $\vec{r}$ is the location of an object at a given time $t$, $\vec{m}$ is the displacement vector, and $\vec{b}$ the starting position.

The values of all vectors and the time are integers.

## Things that didn't work

* The example puzzle input is great to understand the problem, but it is too short for the approach taken here.
* Because of the integer constraint a simple analytical solution of the equations did not work for me.
* I also gave the linear solver **PulP** a try, but it quickly turned out that the problem is not linear.
* For the same reason, running a Gradient Descent did not work (I happened to have a from scratch implementation around, but it got stuck in local minima)

## The idea

Looking at the puzzle input (and the example input), I noticed that there are many hail stones that move at the same speed in x, y or z. They have a constant distance to each other on that axis.
**The relative speed of the rock must divide that distance without remainder.**

If I could find a few such example divisions, I might be able to determine the displacement vector of the rock.

## Variables

I considered each dimension independently:

* $rx(t)$ : x-position of an object at time t
* $brx$ : starting x-coordinate of the rock
* $bsx_i$ : starting x-coordinate of hail stone *i*
* $mrx$ : x-displacement of the rock
* $msx_i$ : x-displacement of hail stone *i*

## Determine the displacement

To find out $mrx$, we look at a pair of hail stones with the same x-speed.
The points where the rock hits them can be described by:

$mrx \cdot t_1 + brx = msx_1 \cdot t_1 + bsx_1$

$mrx \cdot t_2 + brx = msx_2 \cdot t_2 + bsx_2$

Subtracting both equations from each other removes $brx$, the starting point is irrelevant for now:

$mrx (t_1 - t_2) = msx_1 \cdot t_1 + bsx_1 - msx_2 \cdot t_2 - bsx_2$

Because both stones move at the same speed ($msx_1 = msx_2$), it simplifies to:

$mrx (t_1 - t_2) = msx (t_1 - t_2) + bsx_1 - bsx_2$

Replacing the time difference by $\Delta t$:

$mrx \Delta t = msx \Delta t + bsx_1 - bsx_2$


or, isolating the time difference:

$$\Delta t = \frac{bsx_1 - bsx_2}{mrx - msx}$$

Because we know that the time difference $\Delta t$ must be integer, we are looking for valid values for $mrx$ that we can insert into the equation and get a clean integer.

If you have3 multiple pairs of hail stones with the same $msx$, you can determine the **greatest common denominators** of the $bsx$ differences for two respective pairs. This is not a mathematically super clean approach, because the real denominator could be smaller. So it does not have to fit for all examples.

Note that the denominator sometimes may be both positive and negative, it does not matter.

This involves a bit of trial and error and a bit of guesswork. I printed all denominators and the resulting possible values for $mrx$ and scanned the result by eyeball.

If you have a guess for $mrx$ you can check it by inserting it back into the equation for $\Delta t$. The result should be an integer in all cases.

Proceed in the same way for the y and z dimensions.

## Determine the starting position

Now that I knew the complete vector $\vec{mr}$, I could start looking for the starting position $\vec{br}$ (the intercept in the linear equation above). This requires combining the three dimensions. At this point I was tired and messed up the equation 3 times.

There is a simple and a less simple algebraic solution:

### Simple solution

If you are lucky, there is a hail stone with exactly the same displacement in one dimension as the rock, e.g.:

$mrx = msx$

Such a hail stone has to be hit at $t=0$, otherwise the rock would never reach it.
There you have your starting position.

### Algebraic solution

We again consider a rock that is hit by a hail stone at $t > 0$:

$mrx \cdot t + brx = msx \cdot t + bsx$

Isolating $t$ gives

$$t = \frac{bsx - brx}{mrx - msx}$$

The collision time is the same for all dimensions:

$$t = \frac{bsx - brx}{mrx - msx} = \frac{bsy - bry}{mry - msy} = \frac{bsz - brz}{mrz - msz}$$

To proceed, we need to consider two dimensions and ignore the rest:

$$\frac{bsx - brx}{mrx - msx} = \frac{bsy - bry}{mry - msy}$$

Now we have an equation with two unknown variables ($brx$ and $bry$). The rest is known.

Bring $bry$ on one side:

$$bry = bsy - \frac{(bsx - brx) \cdot (mry - msy)}{mrx - msx}$$


To resolve the unknown variables, we consider any two hail stones. This removes $bry$ from the equation:

$$bsy_1 - \frac{(bsx_1 - brx) \cdot (mry - msy_1)}{mrx - msx_1} = bsy_2 - \frac{(bsx_2 - brx) \cdot (mry - msy_2)}{mrx - msx_2}$$

To keep the equation manageable, I replaced the slope terms (that won't change anyway):

$$\alpha = \frac{mry - msy_1}{mrx - msx_1}$$

$$\beta = \frac{mry - msy_2}{mrx - msx_2}$$

so that

$$bsy_1 - (bsx_1 - brx) \cdot \alpha = bsy_2 - (bsx_2 - brx) \cdot \beta$$

Finding $brx$ is now a matter of diligence and careful information. From here it goes downhill.

**Have fun implementing!**