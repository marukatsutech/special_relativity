# Special relativity: Why is the speed of light constant?
# Chapter - 1. Light sphere

## 1. Introduction
Einstein's principle of the constancy of the speed of light is a principle, 
but it does not explain why the speed of light is constant. 
Here, I would like to consider why the speed of light is constant.

## 2. Overview of the principle of light speed constancy
Why is the speed of light constant? The answer is simple.
That is observable fact in our world.
Based on Einstein’s principle of constancy of light velocity,
time dilation and length contraction will happen when we travel nearly lightspeed.

![image_ch1_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch1_fig2-1.png)

Fig. 2-1. Lorentz transformation and  Minkowski spacetime

## 3. Light-Sphere
Why is the speed of light same to observers moving at different speed (one in a rocket and the other on the earth)?
What does not change depending on the viewpoint……
They are circles (spheres)!!

![image_ch1_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch1_fig2-2.png)

Fig. 2-2. Lorentz transformation and Light-sphere transformation

![image_fig1-1](https://github.com/marukatsutech/special_relativity/blob/main/image_fig1-1.png)

Fig. 2-3. Light-sphere (Light spreading spherically in Minkowski space)

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/main/image_special-relativity.png)

Fig. 2-4. Light-sphere transformation in Minkowski space and moiré pattern

## 4. Conclusion
My idea is as following.
Light(Photon) is not a dot but a sphere that expands in Minkowski spacetime. 
* Light(Photon) is not a dot but a sphere.
* We can only observe our world with discretization (quantization)  just like moire pattern.
* That is why light speed does not change depending on the viewpoint of every observers.

Watch my video for more detail!

[(https://youtu.be/AwRgGn6AzzU)](https://youtu.be/AwRgGn6AzzU)

Light-sphere - Special relativity-1: Why is the speed of light constant?

## Python exercise - 34  
Simple exercise of matplotlib-animation of Python.

### Source code
files:  
* special_relativity_moire.py : The similarity of Minkowski spacetime and moire pattern
* special_relativuty_rot.py : Lorentz transformation and rotation
* special_relativity.py : Lorentz transformation

## Reference
* Wikipedia: Special relativity
https://en.wikipedia.org/wiki/Special_relativity
* Wikipedia: Lorentz transformation
https://en.wikipedia.org/wiki/Lorentz_transformation
* Wikipedia: Minkowski space
https://en.wikipedia.org/wiki/Minkowski_space
* Wikipedia: Moiré pattern
https://en.wikipedia.org/wiki/Moir%C3%A9_pattern

# Chapter - 2. Light arrow - The mechanism by which light spreading out as a sphere is observed at a single point.

Watch my video for overview!

[(https://youtu.be/aw-4OaHOQQU)](https://youtu.be/aw-4OaHOQQU)

Light arrow - Special relativity - 2: The mechanism of light speed

## 1. Introduction
My argument in the last video (chapter - 1)was that light is a sphere spread out in Minkowski space(Fig 1-1). However, in reality, light is observed not as a surface but as a point. Regarding this, in the previous video, I only suggested that we could see what appeared to be light trajectories through the moiré patterns (interference fringes) created by concentric circles and stripes(Fig 1-2). This time, we will consider the mechanism by which light spreading out as a sphere is observed at a single point.

![image_fig1-1](https://github.com/marukatsutech/special_relativity/blob/main/image_fig1-1.png)

Fig. 1-1. Light-sphere (Light spreading spherically in Minkowski space)

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/master/image_special-relativity.png)

Fig. 1-2. Light-sphere transformation in Minkowski space and moiré pattern

## 2. Huygens-Fresnel principle in Minkowski space
Let's apply the Huygens-Fresnel principle to how waves propagate in Minkowski space.
Here, for simplicity, we will reduce the dimensions and consider a plane (two dimensions). First, when light is generated, it spreads out as a circle in a certain space (hereinafter referred to as light-speed-space). Here, for light, neither time nor space is fixed.
If this is observed from the standpoint of observer A,  the light seen from the observer will be as shown in the figure(Fig 2-1). (Although the space-time coordinates of observer B, who has a different relative speed than observer A, are tilted with respect to the space-time coordinates of A, the light spreads in a circle, so the light appears the same to both observers A and B.).

![image_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-1.png)

Fig. 2-1. Light circle seen from observers A and B

Next, we will look at how light spreads when viewed from observer A. Assuming that the length of each arrow is 1(Fig 2-2a), each arrow indicates the direction (velocity) in which light spreads. In Minkowski space, the slope of a straight line indicating the movement of an object indicates its speed, and a slope of 1 indicates the speed of light, so the speed of a light arrow that spreads out in a circular shape (hereinafter referred to as light-arrow) is equal to the slope of light-arrow from the standpoint of observer A. From then on, it should appear to progress from 0 to ± infinity.
In Minkowski space, the region exceeding the speed of light (slope = 1) is called a spacelike region, and is ignored because the law of causality does not hold, but here we will proceed with the idea without ignoring it and assuming that superluminal speed exists.

![image_fig2-2a](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-2a.png)

Fig. 2-2a. The light circle (light-arrow) seen by the observer

(Try light_arrows.py for Fig 2-2a.)

The arrival point of each light-arrow for observer A at time t=1 is plotted on the straight line at time t=1 as shown in Fig 2-2.b This is like a Mercator projection map that represents the spherical Earth on a flat surface.

![image_fig2-2b](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-2b.png)

Fig. 2-2b. How the light circle spreads as seen by the observer 

(Try light_arrows.py for Fig 2-2b.)


According to the Huygens-Fresnel principle, the wavefront at the next moment is formed by the overlap of circular secondary waves (elementary waves) from each point on the wavefront(Fig 2-3). 

![image_fig2-3](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-3.png)

Fig. 2-3. How secondary waves of light (elementary waves) spread in the speed-of-light space 

(Try light_arrows.py for Fig 2-3.)

Therefore, a wave spreads out in a circle from each point at time t = 1, and the circular wave is plotted in a straight line at time t = 2 in Minkowski space(Fig 2-4, 2-5). In this way, a wave that spreads circularly in light-speed-space will spread flatly in Minkowski space.

![image_fig2-4](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-4.png)

Fig. 2-4. How secondary waves (elementary waves) of light spread as seen from the observer in Minkowski space 
(Try light_arrows.py for Fig 2-4.)

![image_fig2-5](https://github.com/marukatsutech/special_relativity/blob/main/image_fig2-5.png)

Fig. 2-5. Waves spreading in a plane in Minkowski space 

(Try Huygens–Fresnel_Minkowski_space.py for Fig 2-5.)

## 3. Wave superposition and delta function
It turns out that a wave of light that spreads out in a circle spreads out in a plane in Minkowski space. Next, we need to converge the waves on this plane to a single point. The delta function(Fig 3-1, 3-2.) is a superposition of waves with an infinite frequency band.

![image_fig3-1_3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_fig3-1_3-2.png)

Fig. 3-1, 3-2. Superposition of waves

(Try superposed_wave.py for Fig 3-1, 3-2.)

Fortunately, as mentioned above, the slope (= velocity) of light-arrow, which is the element of the wave that spreads circularly in Minkowski space, appears from 0 to ± infinity speed from observer A, so this Let's use 0 to ± infinity to realize the superposition of waves with an infinite frequency width.
The equation of the wave in Fig 3-3 is as follows(Equation 3-1). This is because in order to make it easier to see how circular light spreads out into a flat plane, the speed (=slope) of the light-arrow was made to match the advance of the phase.

y = cos(2π(kx -ωt))  ...Equation 3-1
 k (wave number) = 1 / slope (=reciprocal of the slope of the arrow of light)
 ω (angular frequency) = 1

 Note; The reason for multiplying by 2π is to adjust the phase so that when it advances by 1 in the x
         direction, the phase rotates once (one period of the wave).

The phase velocity vp (Phase velocity) of the wave expressed by the equation of 
y = cos(kx - ωt)) ...Equation 3-2 (k: wavenumber, ω: angular frequency)  is as follows.

vp = ω / k …Equation 3-3

Since the wave number k of the wave corresponding to each light-arrow is k(n) = 1 / slope(n), the phase velocity of each wave is as follows(Equation 3-4), and if the fundamental angular frequency ω(n) is 1, then The speed of each wave is the slope of light-arrow = the speed of light (here, the speed of light is not constant, but ranges from 0 to ± infinity).

vp(n) = ω * slope(n) …Equation 3-4

Note; (n) is a suffix, and the variables with (n) hereafter represent the physical quantities of each light-arrow (n = 0 to ± infinity) and the corresponding wave.
      So, slope(n) = n (= 0 to ± infinity)

Then, if we superpose these waves with wave numbers 0 to ±infinity (the equation is as follows), can we obtain a delta function?

y(n) = cos(2π(k(n)x - ω(n)t))…Equation 3-5
  k(n) =1 / slope(n) (= reciprocal of the slope of the arrow of light), ω(n)=1 
 
Unfortunately, since the phase velocities are different, as time progresses, the phases shift and the peak collapses.

![image_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_fig3-3.png)

Fig. 3-3. Superposition of waves with k(n) =1 /slope(n),　ωn= 1 

(Try light_speed.py for Fig 3-3.)

Furthermore, although the phase velocity is proportional to the slope of light-arrow, the fact that the angular frequency corresponding to the traveling velocity of the traveling wave (Equation 3-6) is constant is not worth removing the limit of light velocity.

y(t, x ) = f (x − vt)　…Equation 3-6

Now, let's assume that ω is proportional to the speed (= slope) of light-arrow. The wave equation in this case is as below.

y(n) = cos(2π(k(n)x - ω(n)t)) …Equation 3-7
 k(n) = 1 / slope(n) (= reciprocal of the slope of the arrow), ω(n) = slope(n) 

In this case, k(n) = 1 / slope(n), ω(n) = slope(n), so the phase velocity vp(n) = ω(n) / k(n) = slope(n) ** 2, which is the square of the slope of the light-arrow, and in this case However, as time progresses, the phase shifts and the peak collapses.

![image_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_fig3-4.png)

Fig. 3-4. Superposition of waves with k(n) =1 /slope(n),　ω(n)= slope(n)

(Try light_speed.py for Fig 3-4.)

So, what is the combination of wave number k and angular frequency ω that does not shift the phase velocity? That is  the group velocities (vp;group velocities) are equal. Group velocity is the traveling speed of a wave packet created by superposition of waves, and can also be said to be the speed at which points with equal phase difference of waves travel, and its formula is as follows.

vg = dω / dk ... Equation 3-8

When applied to this case, it is sufficient to satisfy the following conditions in which the standards ω and k are each 1, and in the simplest case, ω(n) = k(n).

(ω(n) - 1) / (k(n) - 1) = constant ... Equation 3-9

When ω(n) = k(n), the wave equation is as follows.

y(n) = cos(2π(k(n)x - ω(n)t)) ... Equation 3-10,
 k(n) =  ω(n) = slope(n) = n (n = 0 to ± infinity)

So, the equation of the superposed wave of Equation 3-10 is as following.

![image_equation3-11](https://github.com/marukatsutech/special_relativity/blob/main/image_equation3-11.png)

... Equation 3-11
 
Furthermore, since the phase velocity in this case is 

  ω(n) = k(n), vp(n) = ω(n) / k(n) = 1.
  
You can see a wave packet traveling at a phase velocity of 1 while maintaining the peak due to the superposition of waves.

![image_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_fig3-5.png)

Fig. 3-5. Superposition of waves with kn = slope(n),　ωn= slope(n)

(Try light_speed.py for Fig 3-5.)

Now, if we look at the wave equation from earlier,

y(n) = cos(2π(k(n)x - ω(nt))), k(n) = slope(n),　ω(n) = slope(n) ( = k)
  -> y = cos(2π(slope(n) * x - slope(n) * t))
  -> y = cos(2π* slope(n) * (x - t))  ...Equation 3-12

It is a collection of waves with wave number slope(n) times y = cos(2π * (x - t)), so there is no need to bring up group velocity.
Now, in the previous video, three waves were superposed, but let's increase the number of superpositions. 
The following video is a superposition of 100 waves with k(n) = ω(n) = slope(n) (n= 0.1, 0.2, 0.3…~10).

![image_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_fig3-6.png)

Fig. 3-6. Superposition of 100 waves with kn = slope(n),　ωn= slope(n)

(Try light_speed.py for Fig 3-6.)

The peak is clear compared to the superposition of three waves. It is still a superposition of 100 waves and two peaks appear, but if we further increase the number of superpositions and superimpose waves of infinite frequency (corresponding to the slope of light arrow from 0 to ± infinity), we get It should be in the form of a delta function with one peak.

Let us now consider the physical meaning of setting kn = slope(n), ωn = slope(n).
The reason for setting ωn = slope(n) is that we want the slope (=velocity) of the light-arrow to be equal to the traveling speed of the corresponding traveling wave. So what about kn = slope(n)?
Regarding this,in Minkowski space, x (distance) / t (time) = c (speed of light). If the speed of light increases by n times (ωn=slope(n)), the distance traveled (x) needs to increase by n times. This is thought to be because, assuming that the wavelength λ is constant, the distance traveled (x) cannot be multiplied by n unless the wave number is multiplied by n.
The above is the mechanism by which light waves spreading circularly in light-speed-space converge to a single point in Minkowski space.

## 4. Conclusion
In this theory, light spreads in a circular (spherical) manner in light-speed-space, and converges to a single point from the observer's viewpoint (Minkowski space coordinate system) (the trajectory of the convergence point of light is represented on a line in the coordinate system).
Therefore, if the trajectory of the convergence point of light is redrawn so that it looks the same from different observers (different coordinate systems), the result will be the same as Lorentz transformation on Minkowski space.
So why go to the trouble of insisting on this theory?

1) There is no need to treat time in a special way.
In this theory, a four-dimensional light-speed-space exists, and there is no distinction between time and space.
Coordinates (x, y, z, t) depend on the observer's viewpoint.
2) Since light is a circle (sphere) in the light-speed-space, light remains unchanged no matter what viewpoint (coordinate system) it is viewed from.
It's easy to understand if there is.
(The factor that hinders understanding of the special theory of relativity is that the speed of light remains unchanged no matter what coordinate system it is viewed from.(It's hard to understand)
3) Good compatibility with quantum mechanics.
This theory states that light converges to a single point due to the superposition of waves. 
The superposition of waves is a method used in quantum mechanics. 
In this theory, spherical light waves are mapped onto a plane in Minkowski space. It is strange that waves suddenly appear at a distance of - infinity to + infinity.
However, in quantum mechanics, there is a theory called path integral. According to this theory, a quantum is a superposition (integration) of all possible paths before being observed, and the convergence of light in  this theory is inspired by path integral theory.

This is all for my presentation.
Thanks for watching!

## Python exercise - 38
Simple exercise of matplotlib-animation of Python.

### Source code
files: 
* light_arrows.py
* light_speed.py
* Huygens–Fresnel_Minkowski_space.py
* superposed_wave.py

# Chapter - 3. Light arrow and Quantum spin - What are quantum and spin? Bosons and fermions

Watch my video for overview!

[(https://youtu.be/agLXqUW5kyg)](https://youtu.be/agLXqUW5kyg)

Light arrow and Quantum spin - Special relativity-3:
What are quantum and spin? Bosons and fermions in Minkowski space

## 1. Introduction
My argument from last time was that light-arrows spreads out in a circular (spherical) manner in light-speed-space, and from the observer's point of view (Minkowski spatial coordinate system) it spreads out (is projected) as a plane wave, and through superposition, it converges to a single point. 
That's what it meant. Light is one type of quantum called photon, and quantum and photon can be converted into each other through reactions such as pair annihilation and pair creation. If light can be represented as a circle (spherical) in Minkowski space, wouldn't it be possible to represent a quantum with mass like an electron as a light-arrow in light-speed-space?
This time, we will consider quanta that have mass.

Watch my video for overview!  
[https://youtu.be/agLXqUW5kyg](https://youtu.be/agLXqUW5kyg)

## 2. Bosons, fermions and spin
Quantums are classified into bosons, which transmit forces between quanta, and fermions, which make up matter. Photons are bosons that interact with electrons and transmit force; electrons are bosons. In addition, a quantum has a property called spin angular momentum (also simply called spin). The boson's spin is 1, and the fermion's spin is 1/2.

The current explanation of quantum spin is that although it is called spin, it does not mean that the quantum is actually spinning like a ball. However, doesn't the fact that the quantum spin has an angular momentum value lead to some kind of rotation?

![image_ch3_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig2-1.png)

Fig. 2-1. Spin of a photon

Then, what does the spin 1/2 of fermions such as electrons mean? Spin is related to rotational symmetry; a quantum with spin 1 has one-fold rotational symmetry, and a quantum with spin 1/2 has 1/2-fold rotational symmetry. Rotational symmetry refers to how many times a figure becomes indistinguishable during one rotation (360° rotation). 
If it is an equilateral triangle, if it is rotated 120 degrees, it will be in the same state as before the rotation, and it will be in the same state three times within one rotation (rotation 360 degrees), so it has three-fold rotational symmetry.

![image_ch3_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig2-2.png)

Fig. 2-2. Rotational symmetry of figures

Spin 1 means that the object will not be in the same state as before the rotation unless it is rotated once (360 degrees), so if it is spin 1/2, it will not return to its original shape unless it is rotated twice (720 degrees). It cannot be expressed in normal diagrams. 
If it returns to its original state after two revolutions, does spin 1/2 mean a rotation plus a rotation, such as a double rotation(Fig. 2-3), in which rotation is added to the circumference?

![image_ch3_fig2-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig2-3.png)

Fig. 2-3. Double rotation (circumferential rotation)

(Try double_rotation.py for Fig. 2-1.)

## 3. Path integral formulation and spin
Let's now change our perspective and consider the relationship with path integrals. 
The path integral formulation was devised by Richard P. Feynman, and is based on the idea that a quantum takes every possible path between its destination and the point it reaches, and integrates the probability amplitude of the quantum when it takes each path. 
It is said to be equivalent to the Schrödinger equation, which expresses the behavior of a quantum by calculating the probability of existence of a quantum at a point.

![image_ch3_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig3-1.png)

Fig. 3-1. Path integral formulation

I will not explain the formula for the path integral, but what it means is explained in the book THE QUANTUM UNIVERSE (and why anything that can happen, does)　by Brian Cox and Jeff Forshaw. 
According to that work, the change in the phase of the probability amplitude when passing through each path is expressed by the following equation (Equation 3-1), and the sum of the phases is the quantum at the observed position. Indicates the probability of existence.

![image_ch3_eq3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_eq3-1.png)

Equation 3-1.

According to Equation 3-1, the change in the phase of the probability amplitude results in a change in rotation (phase) in proportion to the square of x.

Note: The simulation is shown in the video below, so please refer to that as well.

Python exercise - 25: Quantum mechanics, path integral
https://youtu.be/TTjJU2vyrW4

Python exercise - 30: Quantum mechanics, path integral 2nd
https://youtu.be/U_rPEAHMZpI

## 4. What is spin 1/2?
Now, the probability amplitude of fermions is proportional to the square of x as shown in equation 3-1. Then, can this be expressed by the double rotation (Fig. 2-3) considered in the previous section?

In the case of a light circle, it is represented by a normal rotation and is projected onto the observer's spatial axis in proportion to the slope of the light-arrows that make up the light circle. (Fig 4-4a). 
In the case of fermions, since it is proportional to the square of x, the phase should take a distribution projected onto the x-axis of a parabola, but as shown in Fig. 4-1b, the projection position of the parabola onto the x-axis and the arrow of light If we force the slopes of the arrows to match, the starting points of the arrows will not converge at one point( or a circle), and it seems difficult to represent them with a double rotation like in Fig. 2-3.

![image_ch3_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig4-1.png)

Fig. 4-1a. and 4-1b. Projection of light circle

(Try projection_boson_fermion.py for Fig. 4-1.)

So far, we have only dealt with two dimensions (spatial axis x and time axis t for the observer) in order to simplify the discussion and make it possible to represent it in a plan view. Let's think about adding it.
When the inclination of the arrow of light is expressed as an angle θ from the time axis, the relationship between x and θ is x = tanθ (assuming that the length of the arrow of light = the radius of the light circle is 1). Furthermore, let's assume that the angle θ is from the added spatial axis (referred to as the y-axis) and that the arrow of light rotates like the precession of a top, as shown in Fig. 4-2. At that time, the projection of the arrow of light onto the x-axis is tanθ✕tanθ = x squared.

![image_ch3_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig4-2.png)

Fig. 4−2. Projection of light circle in 3 dimensions - 1

(Try projection_fermion_3d.py for Fig. 4-2.)

In addition, Fig. 4-2 is the same as the arrow of light rotating, just as the spinning top rotates sideways, and its axis of rotation also rotating, which can also be expressed as in Fig. 4-3. In Fig. 4-3, the tip of the arrow of light traces a twisted trajectory like a figure eight. This is thought to indicate the spin of the fermions.

![image_ch3_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig4-3.png)

Fig. 4−3. Projection of light circle in 3 dimensions - 2

(Try projection_fermion_3d_spin.py for Fig. 4-3.)

## 5. Conclusion
* Both bosons and fermions can be represented by light-arrows that spread out spherically in Minkowski space in this theory.
* The difference between bosons and fermions is that bosons have a rotational property on the time and space axes, and fermions also have another rotational property in the spatial direction.

![image_ch3_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig5-1.png)

Fig. 5-1. Spin of boson and fermion

(Try spin_boson_fermion.py for Fig. 4-1.)

## Python exercise - 43
Simple exercise of matplotlib-animation of Python.

### Source code
files: 
double_rotation.py
projection_boson_fermion.py
projection_fermion_3d.py
projection_fermion_3d_spin.py
spin_boson_fermion.py

# Chapter - 4. Relation between special relativity and quantum mechanics
# - wave function collapse and reconsidering of the quantum model -

Watch my video for overview!

[(https://youtu.be/S0RiAzW5u0M)](https://youtu.be/S0RiAzW5u0M)

Relation between Special relativity and Quantum mechanics - Special relativity-4:
Probability, Wave function collapse, Spin and The principle of light speed constancy

## 1. Introduction
In Chapter 2, I explained that light, as a light-arrow, spreads out spherically in light-speed space as a light-sphere, and is projected as a plane wave from the observer's viewpoint (Minkowski space coordinate system), and converges to a single point due to the superposition of waves, which appears the same from any observer. (This is because a sphere appears as a sphere from any direction.)
In addition, in Chapter 3, both bosons and fermions can be represented as a light-arrow that spreads spherically in Minkowski space. The difference between bosons and fermions is that bosons have a rotational property on the time and space axes, while fermions have another rotational property (corresponding to quantum spin), which results in the difference in the properties of bosons and fermions (whether the light-arrow is proportional to x or the square of x when projected onto the space coordinate).
On the other hand, the probability wave shown in Schrodinger's wave equation represents the probability of the existence of a quantum, and it is thought that the wave contracts to a single pointthe moment the quantum is observed (wave function collapse) , but the mechanism by which this contraction occurs is unknown. And if the light-arrow spreads like a wave, similar issues will exist. Therefore, in this chapter, we will reconsider the previous theory from the perspective of the probability of the existence of a quantum.

## 2. Probability of quantum existence
A probability wave does not represent a quantum itself, but the square of the absolute value of the magnitude of the probability wave at a certain position represents the probability (expected value) of finding a quantum at that position (Fig. 2-1). This is called the Born rule, which means that a quantum can only be expressed as a probability, but there are different interpretations of the world represented by the wave function, such as the Copenhagen interpretation and the many-worlds interpretation.

![image_ch4_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig2-1.png)

Fig. 2-1 Probability wave

So, let's think again about what probability is. When we think of probability in our daily lives, we think of the outcome of a coin landing on heads, the number on a dice, or winning a lottery. However, in the world of quantum mechanics, probability is something very mysterious, and that is the interference of probability waves.

The interference of quanta as probability waves can be seen in the double slit experiment. Wave interference at the double slit also occurs in waves on the surface of water, but what is even more mysterious about the interference of quanta as probability waves is that when there is a single quantum, it behaves as if it is interfering with itself. When quanta such as photons or electrons are emitted toward the double slit one by one with a time interval, they are naturally observed as a single point on the observation screen beyond the double slit. When this is repeated, the collection of observed points is distributed across the screen as if waves on the surface of water were interfering with each other at the double slit (Fig. 2-2).

![image_ch4_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig2-2.png)

Fig. 2-2 Double slit experiment

How does the emitted quantum interfere with the quantum emitted before and after it? Does the quantum know the destination of the quantum emitted before and after it and interfere with it by going back and forth in time, or does one particle pass through both slits at the same time? Both are difficult to imagine, but Schrödinger's equation explains (calculates) that a probability wave of one quantum spreads in space and passes through both slits at the same time, and these probability waves interfere with each other. Next, let's reconsider the bosons and fermions represented by the Light-arrow from the perspective of probability.

## 3. Reconsidering the photon (boson) model from the perspective of probability
Let's consider photons here. This is because bosons other than photons (Z bosons, W bosons) have mass, so they are thought to work in a different mechanism than photons and gluons, which have no mass. In Chapter 3, I explained that the light-arrow of photons rotates as shown in Chapter 3 Fig. 4-1 and spreads out in a spherical shape as a light-sphere. However, rotation is a continuous movement, which is inconsistent with the perspective of probability, which is basically random.

In that case, it is sufficient to assume that the Light-arrow does not rotate, but changes its direction (phase) randomly (Fig. 3-1). However, photons have vibrational energy (in visible light, they are observed as the color of light; the shorter the wavelength = the higher the frequency, the higher the energy), and the phase of the vibration changes continuously in space. When the direction of the Light-arrow changes randomly, if the phase of the vibrational energy of the light changes synchronized with Light-arrow-phase, it can be considered to be the same as rotating.

![image_ch4_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-1.png)

Fig. 3-1 Random motion of Light-arrow

(Try photon_probability.py for Fig. 3-1.)

Since there are two phases here, in order to distinguish between them, we will call the phase of the light frequency energy the Light-phase, and the direction of the Light-arrow the Light-arrow-phase. The Light-arrow can be expressed as a rotating vector with the frequency (rotation speed) of light. And a photon is a rotating vector whose phase (Light-arrow-phase) changes randomly as it draws a Light-sphere.

By the way, so far I have not explained how the lower hemisphere of the Light-sphere is projected into space. Regarding the Light-arrow oriented in the lower hemisphere, you may feel that there is no projection destination in the direction of the arrow (it is projected in the direction of negative time). This can be explained from the observer's position (coordinates) with respect to the light-sphere.
When viewed from the observer's coordinates, the slope of the light-arrow (= position / time) indicates the speed. The slope of the Light-arrow in the third quadrant is space (minus) / time (minus) = velocity plus, and the Light-arrow is projected to the first quadrant side. The slope of the light arrow in the fourth quadrant is space (plus) / time (minus) = velocity minus, and the light arrow will be projected toward the second quadrant.

Next, consider the interference of probability waves. If we assume that one photon is composed of multiple light-arrows and that the light-arrows interfere with each other, we can easily explain interference. However, the randomly scattered light-arrows need to come together at the moment they are observed, and the same problem as wave function collapse remains. Considering the of wave function collapse, it is easier to explain Light-arrow in one form.

A case in which one object is observed to interfere is a case in which the objects move around at high speed.
For example, let's put an ant in a box with grids and observe in which cell it can be found (assuming that this ant can move around at high speed). If ants do not have a preference for cells, such as preferring the corners of a box, the probability of the direction at which the ant passes through any cell is equal. Then, place food (sugar, etc.) and obstacles in some cells. Depending on the cell, there is a bias in the frequency of the direction (angle) at which the ant passes by (Fig. 3-2).

![image_ch4_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-2.png)

Fig. 3-2 Random walk ant

Next, randomly select a square and catch the ant with tweezers. The direction of the opening of the tweezers must be kept constant. Also, if the opening of the tweezers do not open wider than the width of the ant, the ant can be caught only if the direction of the opening of the tweezers matches the direction in which the ant passes by(Fig. 3-3). 

![image_ch4_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-3.png)

Fig. 3-3 Catch the random walk ant with tweezers

The more frequently the direction in which the ant passes matches the direction of the tweezers' opening, the higher the probability of catching the ant (Fig. 3-4).
In this case, one object causes interference and probabilistic observation results can be obtained(an ant is a photon, a tweezers is a fermion).

![image_ch4_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-4.png)

Fig. 3-4 Interference of the random walk ant

If we consider that a photon is something whose phase (Light-arrow-phase) changes randomly and rapidly, as if one Light-arrow draws a Light-sphere(Fig. 3-5), then one photon interferes like a wave.  It can also be explained that when observed, it converges to one (wave function collapse).
What is meant by "keep the direction of the tweezers' opening in a constant direction" will be explained in Section 5.

Note that if you take a long-exposure photo of this one ant, you will see afterimages of multiple ants in each cell. Some of the cells show the ant passing in the same direction, while others show them in different directions. The image taken with this long exposure corresponds to the probability wave of the wave function.

![image_ch4_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-5.png)

Fig. 3-5 Photon model

(Try photon_model.py for Fig. 3-5.)

## 4. Reconsidering the fermion model from the perspective of probability
I explained that fermions have one more rotation component (corresponding to quantum spin) in addition to the rotation component that bosons have, and that the Light-arrow rotates in a figure eight shape as shown in Fig. 4-1 in Chaper 3.　However, in the same way that we considered in the previous section that the light-arrow of a photon changes randomly to draw a Light-shere, it is difficult to imagine that the Light-arrow-phase changes randomly and in a figure-eight pattern.
In addition, time and space in the Light-sphere are exactly the same thing, and it is only from the observation viewpoint (the observation coordinates) that the direction of the time axis (orthogonal to it is the space axis) is determined (or appears to be determined), and there is no explanation for why the axis of rotation of quantum spin is always the time axis, as in Fig. 4-1 in Chaper 3.

Therefore, we reconsider the axis of rotation of quantum spin and consider that the light-arrow rotates minutely like the precession of a top, and that the axis of rotation is the axis of rotation of quantum spin.
(In the previous section, the Light-arrow does not rotate but changes randomly, but can be considered to rotate because the Light-arrow-phase changes. In the same way, this precession is also thought to change randomly, not rotate.)


![image_ch4_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig4-1.png)

Fig. 4-1 Precession of Light-Arrow

(Try fermion_model.py for Fig 4-1.)

The tiny rotations caused by the Light-arrow accompanied by precession appear to spread throughout the Light-sphere, and can be seen as a group of rotations because the Light-arrow-phase changes randomly and rapidly as explained in the previous section.
Then,if you focus on a point on the Light-Sphere (the point indicated by the direction of the Light-Arrow), as that point moves a small distance it will make a small rotation, causing it to curve slightly as it moves, appearing to draw a large circle. (To repeat, the Light-arrow-phase changes randomly, so it does not actually rotate, but rather appears to rotate because the Light-phase changes synchronized with the changes in the Light-arrow-phase.) Then, when that point reaches the center of the Light-sphere (the equator), it will draw a large circle in the opposite direction. This is because, as explained in the previous section, in the third and fourth quadrants of the coordinate system, the direction of time from the observer's perspective is negative, and the direction of rotation is also reversed (Fig. 4-2). 

![image_ch4_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig4-2.png)

Fig. 4-2 Group of rotations

As a result, the light arrow will form a figure eight, similar to what was explained in Chapter 3. In addition, since the minute rotation due to the precession of the Light-arrow spreads over the entire Light-sphere, no matter where the starting point is, it will always trace a figure eight, and therefore it will always trace the same figure eight from any observer, which is consistent with the relative way of thinking (Fig. 4-3). 

![image_ch4_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig4-3.png)

Fig. 4-3 Rotating vector of Light-arrow of fermions

(Try rotating_vector_fermion.py for Fig 4-3.)

By the way, the shape of the figure eight explained in Chapter 3 is slightly different from the figure eight this time (the circular part of the figure eight this time is a perfect circle). In Chapter 3, I explained that in order for the projection of the light-arrow onto the spatial coordinate to be proportional to the square of the spatial coordinate (x), it is necessary to rotate in a figure-8 pattern. This is because the change in phase w of the probability wave representing the fermion in the path integral is proportional to the square of the spatial coordinate x, as shown by the equation w=mx**2/2ht.
In the case of the figure eight this time, this can be easily explained by the intersection of a cone. Depending on the cut (the angle at which it intersects with the plane), the shape of the cone and its intersectiopn can be a circle, an ellipse, a parabola, or a hyperbola.

Video. Intersection of Cone and Plane (circle, ellipse, parabola and hyperbola)

[https://youtu.be/beXKDRCCzY0](https://youtu.be/beXKDRCCzY0)

And, as explained in the previous section, the Light-arrow can be expressed as a rotating vector, so the infinitesimal rotating vector that rotates (appears to rotate) like a cone due to precession can be considered as a rotating vector centered on the central axis of a figure-8 cone as a whole. This rotating vector is inclined at 45 degrees from the observer's time axis or space axis (Fig. 4-2), which will be important in the next explanation.

Reference; Stokes' theorem (Wikipedia)
The surface integral of the curl of a vector field on a surface is equal to the line integral of the original vector field on the boundary of the surface.
https://en.wikipedia.org/wiki/Stokes%27_theorem

Furthermore, when the Light-arrow as a whole draws a figure eight by connecting two circles, it rotates 720 degrees and returns to its original state, which easily explains the 1/2-fold rotational symmetry of fermions.

## 5. Relation between quantum interactions and the principle of the constancy of the speed of light
Observing the speed of light is the interaction between light and the observer or the detector, and between photons and quanta (mainly electrons) such as cells in the retina or atoms inside the detector's sensor. Therefore, in order to consider the principle of light speed constancy, it is necessary to understand not only the photon but also the mechanism of the observer (quantum) that interacts with the photon. Therefore, in this paper, although it is titled "Special Relativity," I have discussed the nature of the quantum.

In quantum mechanics, the interaction between photons and electrons results in a change in the speed and energy of the quantum before and after the interaction, as explained by the Compton effect, when a photon collides with an electron, and the exchange of momentum in virtual photons exchanged between electrons. (Interactions can also change the type of quantum, such as reactions mediated by the W boson, but we will not discuss these here.)

The probability wave of a quantum (fermion) such as an electron, expressed by the Schrödinger wave function, when simplified to one dimension, is represented by a spiral as shown in Fig. 5-1. The wave is represented by a complex number (real and imaginary parts), and the square of the total absolute value of the complex number indicates the probability that the quantum is observed at that location. The square of the absolute value of a complex number may seem difficult to understand, but the absolute value of that complex number simply refers to the radius of the spiral, as shown in Fig. 5-1. And if a quantum has speed (relative speed) in the spatial direction, the tighter the spiral is (the more turns within the range), the faster it moves.

![image_ch4_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig5-1.png)

Fig. 5-1 Probability wave

A change in the speed of a quantum means that the spiral winding of the probability wave representing the quantum changes, and when a photon interacts with an electron and changes the electron's speed, it means that the photon has the effect of changing (twisting) the spiral winding of the electron's wave function. The video below is a simulation of the behavior of a quantum when a potential is applied to the waveform representing the quantum to change its phase (twist it to change its winding), and in the calculations, the quantum waveform on the left is rotated proportionally to the waveform on the right.

Video. Quantum path integral  in potential

[https://youtu.be/r7ozb2d25hQ](https://youtu.be/r7ozb2d25hQ)

What causes the photon to twist the waveform of the electron is the frequency of the photon. The energy of a photon is expressed as E = hν, and photons with higher frequencies (such as gamma rays) impart more energy when they collide with an electron (they cause a larger change in the electron's speed). The photon vibration (rotation in the direction of the light-phase) also gives a twist to the interaction between photons and electrons (fermions) that make up the light-arrow explained in sections 3 and 4. As explained in section 3, the light-arrow of the photon travels through all space-time in an instant, but this violates the principle of light speed constancy.

However, the fermion light-arrow described in the previous section can be regarded as a rotating vector as a whole that makes a 45 degree angle with the time or space axis. In order to add a twist to the rotation vector, the rotation vector needs to have the same direction as the vector. Therefore, the only thing an electron (fermion) can interact with is the Light-arrow of a photon coming from a 45-degree angle to the time or space axis of the electron (fermion). And moving at a 45-degree angle in Minkowski space means moving at the speed of light (Fig. 5-2).

The same is true for electrons (fermions) that have relative velocity. The world line (time axis) of an electron with a relative velocity appears tilted to a stationary observer. And the rotation vector of the light-arrow of the electron as a whole is tilted at 45 degrees to the world line (time axis) as seen by the electron itself. Therefore, as shown in the figure, it interacts with photons of the light-arrow oriented at that angle. Therefore, the speed of light is observed to be constant from any observer (an electron at rest and an electron with a relative velocity). Furthermore, which electron will interact with which depends on the probability, and the probability is equal. (Fig. 5-2)

![image_ch4_fig5-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig5-2.png)

Fig. 5-2 Rotating vector and interaction

Furthermore, a electron (fermion), which is represented as probability wave, are spread out until it is observed. The same is true for the electron (fermion), which is represented by a Light-arrow. A rotation vector with a small rotation (spin component) changes the Light-arrow-phase randomly and quickly, and since it is projected onto the spatial coordinate system, it travels through all spaces in an instant. Then, at some point, it interacts with the Light-arrow of a photon that is also traveling through all space. Basically, the probability of interaction at any position of the Light-arrow is equal. However, depending on the respective paths taken before the interaction, there are positions where the frequency of the Light-arrows passing back and forth and the frequency of the rotation vectors aligning are higher, and the probability of interaction (being observed) at those positions is higher(Fig 5-3).

![image_ch4_fig5-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig5-3.png)

Fig. 5-3 Light_speed_constancy

(Try special_relativity_rot.py and light_speed_constancy.py for Fig 5-3.)

This is how the principle of light speed constancy works.

By the way, "keep the direction of the tweezers' opening in a constant direction" as explained in Section 3 refers to "the direction of the rotation vector of the fermions as a whole", and also refers to "the stripes" in the "interference fringes of concentric circles and stripes" suggested in Chapter 1.

## 6. Conclusion

* A photon is a rotating vector with the frequency of light, and it changes direction randomly and rapidly.
* Fermions have spin properties, such as precession, and their overall rotation vector is inclined at 45 degrees to the time or space axis.
* Photons and fermions randomly and rapidly change the direction of their rotating vectors, and the slope of the rotating vectors, which represent their speed in Minkowski space, has a speed from 0 to infinity and is projected across the entire space in an instant.
* Photons and fermions projected across the entire space in an instant interact probabilistically when their rotation vectors align.


Why is the speed of light constant?
The answer is that our world is quantized!

# Chapter - 5. Elementary particles

Watch my video for overview!

[(https://youtu.be/Tnjde_0vegs)](https://youtu.be/Tnjde_0vegs)

Elementary particles - Special relativity-5
Oscillation modes, charges, color charges, and color confinement

## 1. Introduction
In the previous chapters, I explained that a photon is a Light-arrow that can be expressed as a rotating vector, and its direction (Light-arrow-phase) changes randomly and rapidly within Minkowski space. I also explained that fermions exhibit fermionic properties due to the minute precession of the light-arrow (minute rotation component = spin) (fig. 1-1). However, the Standard Model of particle physics states that there are 17 types of elementary particles currently considered, including photons, electrons, neutrinos, and quarks, excluding the as-yet-undiscovered graviton (fig. 1-2). If photons and fermions can be explained by the Light-arrow as explained in this theory, then the properties of each elementary particle should also be explained by the Light-arrow. In this chapter, we consider the picture of elementary particles represented by the Light-arrow.

![image_ch5_fig1-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig1-1.png)

Fig. 1-1 Standard Model of particle physics

## 2. Three-axis rotation
Let's consider the mechanism of precession of the Light-arrow explained in the previous chapter in terms of three-axis rotation. Three-axis rotation means rotation around the x-axis, y-axis, and z-axis. An airplane can freely change direction by rotating in three directions: Roll (on the aircraft's forward/backward axis), Pitch (on the aircraft's left/right axis), and Yaw (on the aircraft's up/down axis). 

Here, as shown in fig. 2-1, the orthogonal rotation axes are A-axis, B-axis, and C-axis. The reason why we use the A-axis, B-axis, and C-axis instead of the x-axis, y-axis, and z-axis is that these axes are rotation axes of the elementary particle's own coordinate system (the internal space of the elementary particle), like the roll, pitch, and yaw axes of an airplane, and are to distinguish them from the rotation axes of the external space indicated by the x-axis, y-axis, and z-axis. Furthermore, since Minkowski space is four-dimensional, including the time axis, four orthogonal rotation axes are needed, so a fourth axis (D-axis) is needed. However, since we exist in three-dimensional space, we cannot illustrate four orthogonal axes. Therefore, we can only imagine the D axis, which is perpendicular to the A axis, B axis, and C axis. 

![image_ch5_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig2-1.png)

Fig. 2-1 Roll, pitch, and yaw axes of an airplane

However, as described in the previous chapters, in this theory, space and time are the same thing in Minkowski space, and the spatial and time axes are determined by the observer's position (the direction of movement in Minkowski space-time). Therefore, when three axes are illustrated on a diagram, they represent two spatial axes and a time axis, and it is believed that the same relationship will result regardless of which combination of three of the four rotation axes is illustrated, as in fig. 2-2. 

![image_ch5_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig2-2.png)

Fig. 2-2 Relation betweeen three spatial axes and time axis

Now, we will show these rotations in the A-axis, B-axis, and C-axis directions as rotation vectors with dotted arrows, and from now on we will call them rotation vector A, rotation vector B, and rotation vector C. The direction of these arrows indicates the direction of rotation (generally the direction of movement when a right-handed screw is turned in physics and mathematics), and the length of the arrows indicates the speed of rotation.　The result of rotation by these three rotation vectors A, B, and C is represented by the resultant rotation vector of rotation vectors A, B, and C.　And this resultant rotation vector can show various orientations in Minkowski space depending on the magnitude (length of the arrow) of each of rotation vectors A, B, and C (fig. 2-3).

![image_ch5_fig2-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig2-3.png)

Fig. 2-3 Resultant rotation vector of vector A, B, and C

## 3. Oscillation modes of rotating vectors
Next, let us oscillate the magnitude of the rotation vectors A, B, and C in a cosine curve shape. Then, the behavior of the resultant rotation vector can be divided into the following patterns (modes).

Oscillation mode 1: Constant(no oscillation)

When the magnitudes of rotation vectors A, B, and C are constant, the resultant rotation vector of rotation vectors A, B, and C shows a constant direction. And A, B, and C-axis that represent the internal coordinate axes of an elementary particle (A, B, C axes) rotate at a constant speed around the resultant rotation vector.

![image_ch5_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig3-1.png)

Fig. 3-1 Oscillation mode 1

Oscillation mode 2: Oscillate and the three oscillation phases are the same.

Rotation vectors A, B, and C are changed into cosine curves. The phases of the three cosine curves are the same. The resultant rotation vector then points in a constant direction. However, unlike oscillation mode 1, the magnitude of the resultant rotation vector (the length of the arrow) changes (oscillates). And the elementary particle (A, B, C axes) rotate and vibrate clockwise and counterclockwise.

![image_ch5_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig3-2.png)

Fig. 3-2 Oscillation mode 2

Oscillation mode 3: Oscillate and the three oscillation phases are shifted by 120 degrees each.

Rotation vectors A, B and C are changed into cosine curves. The phases of the three cosine curves are shifted by 120 degrees each. Then, the resultant rotation vector precesses with a constant magnitude (the length of the arrow). And the elementary particles (A, B, C axes) rotate like precessing tops.

![image_ch5_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig3-3.png)

Fig. 3-3 Oscillation mode 3

Oscillation mode 4: Oscillate only on two axes and the two oscillation phases are shifted by 90 degrees.

Rotation vectors A and B are changed into cosine curves. The phases of the two cosine curves are shifted by 90 degrees. And the oscillation and amplitude of the rotation vector C are zero.
In this case, although the magnitude of precession differs from that in oscillation mode 3, the resultant rotation vector precesses with a constant magnitude.
And the elementary particles (A, B, C axes) rotate like precessing tops.

![image_ch5_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig3-4.png)

Fig. 3-4 Oscillation mode 4

Oscillation mode 5: Oscillate only on one axis.

Rotation vectors A is changed into cosine curves. And the oscillation and amplitude of the rotation vector B and C are zero. The resultant rotation vector shows a constant direction (the same direction as rotation vector A). Then, as in oscillation mode 2, the magnitude of the resultant rotation vector (length of the arrow) changes (vibrates). And the elementary particle (A, B, C axes) rotate and vibrate clockwise and counterclockwise.


![image_ch5_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig3-5.png)

Fig. 3-5 Oscillation mode 5

Let us apply the oscillation modes of rotating vectors described above to elementary particles. 

In oscillation mode 1, the resultant rotating vector faces a fixed direction and does not precess, so this mode is considered to be the state of photons. In oscillation mode 2, the resultant rotation vector faces a fixed direction and does not precess but vibrate. As explained in Chapter 4, in order to interact with photons, the light-arrow needs to precess due to its spin. So this mode is considered to be the state of neutrinos, since they have a speed close to the speed of light and have a weak interaction with matter. Oscillation modes 3 and 4 appear to be electrons or quarks that undergo electromagnetic interactions due to precession, but which is which? And what is oscillation mode 5?

## 4. Relation between oscillation modes of rotating vectors and electric charges
Charge is a quantum property that governs electromagnetic interactions. Electrons have positive charge of 1, up quarks have positive 2/3 charge, and down quarks have negative 1/3 charge.

In oscillation mode IV, the rotation vectors A, B, and C are out of phase with each other by 120 degrees, which is 1/3 of one rotation (360 degrees), evoking the relationship with the positive 2/3 charge (up quark) and negative 1/3 charge (down quark) of a quark (and also with color charge, which will be explained in the next section).

As explained in Chapter 4, if the electromagnetic interaction of electric charge is the probabilistic action of photons on electrons, then the difference in the magnitude of the electric charge between electrons and quarks can be thought of as resulting in a probability difference in receiving the oscillation of the photon, which is a rotating vector.

We will discuss the positive and negative charges later, but the fact that the absolute value of the charge of an electron is greater than that of a quark means that it has a higher probability of receiving photon oscillations (i.e. energy). Taking this into consideration, oscillation mode 3 receives photon oscillations in three axial directions, while oscillation mode 4 receives photon oscillations in two axial directions, so it is thought that the probability of receiving photon vibrations is higher in oscillation mode 3. From this, it is thought that oscillation mode 3 represents electrons and oscillation mode 4 represents quarks.

As mentioned above, the number of axes of the rotating vector is proportional to the charge, so the 3/3 axis (oscillation mode 3) represents electrons with negative 1 charge, and the 2/3 axis represents up quarks with positive 2/3 charge. Then, the down quark with negative 1/3 charge is considered to be a mode in which only one axis oscillates, and this case is called oscillation mode 5. However, in oscillation mode 5, the resultant rotation vector does not precess, so this does not fit the idea of interaction explained in Chapter 4. This will be explained in the next section.

Regarding the positive and negative charges, it is sufficient to consider the positive and negative rotations. Oscillations can be considered as rotation (oscillations can be expressed as rotation on the complex plane. The direction of the imaginary part on the complex plane should be the D-axis direction, which is not shown in the figure). The composition of rotations is mathematically expressed as multiplication. Therefore, if the oscillation (rotation) of one axis is a negative charge, the oscillation of two axes is negative x negative = positive, and the oscillation of three axes is negative x negative x negative = negative.

## 5. Relation between oscillation modes of rotating vectors and color charges, and color confinement
Is oscillation mode 5, which oscillates on only one axis, a down quark? Let's consider this from the perspective of color charge and color confinement.

Hadrons such as protons and neutrons are thought to be made up of quarks. Protons are made up of two up quarks and one down quark (u,u,d), and neutrons are made up of one up quark and two down quarks (u,d,d).

![image_ch5_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig5-1.png)

Fig. 5-1 Protons and neutrons

However, quarks cannot exist as independent elementary particles; they only exist as building blocks of hadrons. The principle behind this is thought to be color confinement. Quarks have the color charges red, green, blue, anti-red, anti-green, and anti-blue. In hadrons such as protons and neutrons, it is thought that the red, green, and blue color charges of the three quarks that make up them are neutralized to become white, confining the quarks (however, quarks do not actually have color. This is an analogy for the fact that the three primary colors of light, red, green, and blue, combine to produce white light.). In addition, the interaction between quarks is carried out by gluons, which are called the strong interaction, and gluons are also said to have color charge.

As mentioned in Section 4, if elementary particles can be expressed as oscillation modes of three rotating vectors (four axes including time), how should we think about the structure of hadrons, which are made up of quarks such as protons and neutrons? The answer lies in electrons.

Considering that photons, neutrinos, and electrons exist stably (have no life span and do not decay), we should consider that the three oscillation modes that can exist stably in the space-time that is our universe are oscillation mode 1 (zero oscillation of the rotation vector on the three axes), oscillation mode 2 (all three axes oscllate in phase), and oscillation mode 3 (the three axes oscllate out of phase shifted by 120 degrees each).
In protons and neutrons, oscillation mode 3, which corresponds to the oscillation mode of the electron, is thought to be responsible for color confinement.

First, consider the case of a proton (u,u,d). It is thought that the proton is formed by confining part of the oscillation axes of quarks in oscillation mode 3. As shown in the figure, two space axes and one space axis and one time axis are shared to form oscillation mode 3. Since the up quark oscillates on the 2 space axis + 1 time axis, it has a positive 2/3 charge. The down quark has a positive charge of 2/3, but oscillation mode 3 has a negative charge of 3/3, totaling a negative charge of 1/3.

![image_ch5_fig5-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig5-2.png)

Fig. 5-2 Protons model

Next, consider the case of neutrons (u,u,d). In the case of neutrons, one up quark shares one space axis and two down quarks share one space axis and one time axis, forming oscillation mode 3. Because of this extra time axis, the charge of oscillation mode 3 is negative 3/3 x two times = negative 6/3. This extra time axis makes oscillation mode 3 unstable, so the neutron lifetime is short.

![image_ch5_fig5-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig5-3.png)

Fig. 5-3 Neutrons model

## 6. Conclusion
* Elementary particles can be expressed as a resultant vector of rotation vectors in four axial directions (three spatial axes plus one time axis), and the characteristics of the elementary particles depend on the type of oscillation mode of the rotation vector in each axial direction.
* Oscillation mode 1 represents photons, oscillation mode 2 represents neutrinos, oscillation mode 3 represents electrons.
* Color confinement of quarks occurs via oscillation mode 3 in the case of protons and neutrons.
* Quarks originally have rotation vectors that oscillate along four axes. The axes shared from quarks when forming protons and neutrons behaves like an electron (= oscillation mode 3).
* The up quark shares the 1 spatial axis from the 4 axes with oscillation mode 3, which causes color confinement. Then, the rotation vector oscillates on the 2 spatial axes + 1 time axis, which are not shared, and has a positive 2/3 charge.
* The down quark shares the 1 spatial axis and 1 time axis from the 4 axes with oscillation mode 3, which causes color confinement. Then, the rotation vector oscillates on the unshared 2 spatial axes and the 1 time axis, which is confined by color confinement, so it also has a positive 2/3 charge. However, oscillation mode 3, which causes color confinement, is equivalent to an electron and has a total negative 1/3 charge.
* When the color confinement constraints are released, the quarks revert to their original four-axis oscillation mode and immediately transform into other elementary particles. Therefore, quarks do not exist alone.

So, as mentioned above, photons, neutrinos, up quarks, and down quarks can be explained as oscillations of a rotating vector, but how do other elementary particles work?

It is believed that gluons are responsible for the interactions between quarks, but in this theory gluons are not necessary, and it is thought that the oscillation fluctuations that occur when the constraints of oscillation mode 3 are disturbed are expressed as quantum phenomena.

As for the W and Z bosons, since these elementary particles can only be observed indirectly by decaying into other elementary particles, they can be thought of as quantum representations of the oscillations that occur when oscillation mode 3 becomes disordered and breaks up and reconstructs, just like gluons. However, this can also be explained as follows.

The W boson is thought to be composed of an electron (or positron) and an electron neutrino because it splits into them.

However, considering that the lifetime of the W boson is very short, the oscillation mode of the trapped axes are not constrained as oscillation mode 3, but rather, just as there is an extra axis constrained by the neutron, one axis of the neutrino is captured by the electron (or, conversely, one axis of the electron is captured by the neutrino, or they alternately capture and share each other's axes).

The Z boson decays into a pair of antiparticles. Since the Z boson has a very short lifetime, it is thought that, like the W boson mentioned above, one of the particles captures one axis, or they alternately share the axis.

In addition, since both the W boson and the Z boson have zero spin, the constituent particles are thought to have spins pointing up and down, canceling each other out. It is also thought that the particles have a large mass due to their rotation (orbital angular momentum) when bound together.
The three generations of elementary particles are thought to be related to the frequencies of the oscillation modes and their standing waves, but further consideration is needed.

![image_ch5_fig6-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch5_fig6-1.png)

Fig. 5-3 oscillation modes and standard model of elementary particles physics

# Chapter - 6. Quantum spin and Light speed constancy
How the principle of light speed constancy works.

Watch my video for overview!

[(https://youtu.be/EsmJpV8vKCc)](https://youtu.be/EsmJpV8vKCc)

## 1. Introduction
In Chapter 5, we considered the nature of elementary particles from the perspective of the oscillation modes of rotating vectors.

In this chapter we further consider oscillation modes.

We will then look back on our considerations so far and reconsider the principle of light speed constancy, which was the starting point of this theory and was discussed in Chapter 4 - The relationship between quantum mechanics and special relativity.

## 2. Charges, Interactions, and Space-Time Axes
In elementary particles that undergo electromagnetic interactions, such as electrons and quarks, Coulomb forces occur between the particles due to their electric charges.
Coulomb force is a repulsive force between the same charges, such as positive charge and positive charge, or negative charge and negative charge, but an attractive force occurs between different charges, such as positive charge and negative charge.

![image_ch6_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig2-1.png)

Fig. 2-1 Positive and negative charges

In quantum field theory (quantum electrodynamics), the Coulomb force is carried out by virtual photons that arise between elementary particles.
For example, in the case of electrons, the virtual photon generated between the electrons collides with the electron, giving it kinetic energy and generating a repulsive force.
So, how can we explain the electromagnetic interaction of electric charges if we represent elementary particles in terms of oscillation modes?

![image_ch6_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig2-2.png)

Fig. 2-2 Interaction of electrons and photons

In Chapter 5, I explained that the mechanism behind the positive and negative charges of electrons and quarks is related to the number of axes of oscillation (rotation). 
If the oscillation (rotation) of one axis is considered to be a negative charge, then the oscillation of two axes is negative x negative = positive, and the oscllation of three axes is negative x negative x negative = negative.
Since a virtual photon collides with an electron and exerts a repulsive force (moving in the opposite direction), the essence of the action of electric charges seems to be to reverse something. Then, how should we think about the attractive force?

When considering the vector of the force direction in a two-dimensional plane, the direction can be reversed by rotating the vector by 180 degrees.
In three dimensions, the direction of a vector can also be changed by inverting it (rotating it 180 degrees) relative to the coordinate axis.
First, the initial direction of the vector is set to negative (if the C axis is considered to represent time as in Minkowski space, this results in a negative velocity).
If it is then rotated 180 degrees around the A axis and then around the B axis, it will be inverted from its initial position with the C axis as the axis of symmetry and will point in the positive direction.

If it is then rotated a further 180 degrees around the C axis, it will return to its original negative orientation.
In this way, the space-time axis and electric charge are closely related, and electromagnetic interaction is the reversal (180 degree rotation) of the direction of oscillation(rotation). The positive/negative and magnitude of the electric charge depend on the number of rotation axes (degrees of freedom of rotation).

![image_ch6_fig2-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig2-3.png)

Fig. 2-3 Positive and negative charges in Minkowski space

(Try electric_charges_interaction.py for Fig 2-3.)

## 3. Oscillation modes and rotation operation
In Chapter 4, I considered that spin, a property of fermions, is the infinitesimal precession of a rotating vector. 
I explained that the direction of the precessing rotating vector changes rapidly and randomly, resulting in superposition, resulting in a large overall precession angle of 45 degrees (however, I did not fully consider how this works).

In Chapter 5, I explained that elementary particles can be expressed as oscillation modes of rotating vectors on four axes (three spatial axes plus the time axis). 
Precession appears in oscillation modes 3 and 4. 
However, the angle of precession is too large to be considered infinitesimal. 
Moreover, in oscilattion mode 4, which is thought to represent the up quark, the angle of precession is 45 degrees.

The consideration that fermions have a 45 degree precession angle is the basis of the principle of  light speed constancy explained in Chapter 4. Therefore, we will consider why oscillation mode 4 precesses at a 45 degree angle.

In oscillation mode 4, the oscillations of rotation vectors A and B are out of phase with each other by 90 degrees.
The phase shift of 90 degrees is the same as the relationship between the sine and cosine curves of rotational motion.

![image_ch6_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-1.png)

Fig. 3-1 Phase shift of oscillation mode 4

Now, let's simulate the behavior of the rotation vector using only rotation operations, as follows.
 Let the rotation vector equivalent to the resultant rotation vector of oscillation mode 4 be rotation vector A-B. 
Then, rotate rotation vector A-B within plane A-B around axis C. 
Next, rotate all the coordinate axes around rotation vector A-B. Then, just like oscillation mode 4, it undergoes precession at an angle of 45 degrees.

![image_ch6_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-2.png)

Fig. 3-2 Rotation operations

(Try precession_rotation.py for Fig 3-2.)

This is simply the resultant rotation vector of rotation vector A-B and rotation vector C, and if rotation vector A-B and rotation vector C are orthogonal and have the same length (= same rotation speed), then the resultant rotation vector will be 45 degrees as shown in the figure.

![image_ch6_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-3.png)

Fig. 3-3 Resultant rotation vector

In the case of oscillation mode 3, the oscillation phases of rotation vectors A, B, and C are shifted by 120 degrees, so the resultant rotation vector maintains the same length and rotates. However, because the length of the resultant rotation vector is longer than 1, the angle of precession is smaller than 45 degrees.

![image_ch6_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-4.png)

Fig. 3-4 Resultant rotation vector of oscillation mode 3

In any case, when the rotation vector is rotated around an axis perpendicular to its direction, it undergoes precession.
This is a double rotation, which adds another rotation to the rotation, and is consistent with what was explained in Chapter 3: single rotation is for photons and double rotation is for fermions, and the number of rotations is related to quantum spin.

![image_ch3_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch3_fig5-1.png)

Fig. 3-4-1 Spin of boson and fermion (same as fig.5-1 in chapter 3)

The direction of the rotation vector will be the same regardless of its orientation as long as the orthogonal relationship is maintained, so we will simulate it by replacing it with rotation operations along the A-axis, B-axis, and C-axis, which are the internal coordinates of the elementary particle.
As is obvious, when rotating around two axes, precession occurs at an angle of 45 degrees.

![image_ch6_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-5.png)

Fig. 3-5 Rotation of axes

(Try axes_rotation.py for Fig 3-5.)

Next, we perform rotation around three axes. 
Since oscillation mode 4, which is equivalent to rotation around two axes (= positive charge 2/3), is set as the up quark, the rotation around three axes should be the electron. 
However, the result of the simulation of rotation around three axes is the same as that in Chapter 5, where oscillation mode 1 (no oscillation) was considered to be a photon.

In retrospect, this is obvious, but the above is self-evident from the rules for vector composition. 
Unfortunately, the precession of the composite rotating vector of three axes is not 45 degrees.
Is it possible to represent elementary particles using the oscillation modes and rotation operations of rotating vectors? 
However, from the discussion so far, it seems that rotation operations are closely related to electric charges and quantum spin.

![image_ch6_fig3-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig3-6.png)

Fig. 3-6 Resultant rotation vector of three axes rotation

## 4. Time axis rotation vector and spin
Next, let us consider the manipulation of rotation vectors, including the time axis rotation vector.
First, a photon can be expressed as a single rotating vector. 
Since a quantum has the properties of both a particle and a wave, if we consider a photon traveling in the A-axis direction as a wave, it oscillates on the spatial axis B and the time axis D as shown in the figure.

![image_ch6_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-1.png)

Fig. 4-1 Photon as light wave

Next, we add rotation to the photon along the time axis (D axis) (add rotation vector D). 
Then, as in the previous discussion, rotation vector A and rotation vector D precess at an angle of 45 degrees.
Now, here is the problem. If we add another rotation vector to rotate around three axes, the precession angle will not be 45 degrees as mentioned in the previous section.

![image_ch6_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-2.png)

Fig. 4-2 Rotation with rotation vector D

Therefore, the pair of rotation vector A and rotation vector D is considered to be one unit (this is called the rotation vector pair A-D).
Then add the rotation vector pair B-D to the rotation vector pair A-D.
Four-dimensional space cannot be drawn strictly, but if we give up on the coincidence of the time axes and prioritize the precession pattern, or prioritize the coincidence of the time axes, we will end up with something like the diagram.

![image_ch6_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-3.png)

Fig. 4-3 Rotation vector pairs

Then, add the rotation vector pair C-D. This too cannot be drawn precisely, and if we maintain the orthogonality of the spatial axes, we cannot make the D axis completely coincident, and part of the D axis can only be drawn overlapping with the C axis.

![image_ch6_fig4-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-4.png)

Fig. 4-4 Electron model with rotation vector pairs

The above theory seems complicated and strange. Also, considering the symmetry of space-time, each axis is thought to precess with space vectors. 
However, vectors can be considered as a combination and can be simplified.
Since all spatial axes are orthogonal to the time axis, we can think of this as a combination of the spatial axis rotation vectors A, B, and C in the rotation vector pair, and the three rotation vectors D in each pair (D in the A-D pair, D in the B-D pair, and D in the C-D pair are considered to be orthogonal to each other).

![image_ch6_fig4-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-5.png)

Fig. 4-5 Spatial and time rotation vectors in rotation vector pairs

And since the resultant rotation vector of the rotation vectors of the three spatial axes and the resultant rotation vector of the three time axes should be orthogonal and of the same length, it can be thought that the whole is precessing at 45 degrees.

![image_ch6_fig4-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig4-6.png)

Fig. 4-6 Precession of resultant rotation vector of spatial and time rotation vector pairs

## 5. Relationship between rotation, charge and spin
The above discussion can be summarized as follows (note that the arrows of the rotation vectors have been omitted).

![image_ch6_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig5-1.png)

Fig. 5-1 Summary of the relation between rotation, charge and spin

The denominator of quantum spin indicates the number of rotation axes of the rotation vector (rotational degrees of freedom), and the number of rotation vector pairs represents the charge.
In addition, the reason why a single rotating vector pair was not considered to be a down quark is that rotating a rotating vector (for example, rotating vector A) in the direction of the D axis, which is the time axis, means rotating it in the plane A-B (or plane C-A) perpendicular to the D axis, which also means rotating it around the C axis perpendicular to the plane A-B. 
Therefore, it was thought that a single rotating vector pair does not exist.
It is also consistent with the color confinement discussed in the next section.

Also, what was oscillation mode 3? 
Oscillation mode 3 was a hint for the idea of color confinement, but it did not fit with the mechanism of the light speed constancy. 
This is because it was simulated with oscillations on three axes. 
Although it is not possible to realize this, oscillations on four orthogonal axes may have produced the same results as above.
(Alternatively, since there are three rotation vector pairs, six axes = six dimensions are required.)

## 6. Reviews of color confinement
n Chapter 5, I explained that oscillation mode 3, which represents electrons, is what causes color confinement. 
However, as explained in the previous section, an electron is made up of three rotating vector pairs, and color confinement is also carried out by three rotating vector pairs.
Therefore, rotating vectors on the time axis are added according to the number of pairs.

![image_ch6_fig6-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig6-1.png)

Fig. 6-1 Reviewed proton model

Also, the reason why the down quark is not treated as a single vector pair is due to the difference in mass (= energy) between up and down quarks, as explained in the previous section. The up quark has a mass of ≃2.2 MeV/c² and a positive charge of 2/3. The down quark has a mass of ≃4.7 MeV/c² and a negative charge of 1/3.
As mentioned above, the charge is the number of rotating vector pairs, and the more the number of rotating vector pairs, the greater the rotational energy (= mass), but this relationship is reversed. 
If we consider the mass of the down quark together with the part equivalent to the electron that functions the color confinement, the mass becomes larger by that amount, which explains the reversal of the relationship between mass and charge.

It is also easily consistent with beta decay, in which a neutron changes into a proton.
If we think about beta decay at the quark level, it is the process in which a down quark changes into an up quark, passing through a W boson and then into an electron and a neutrino, and the down quark can be thought of as containing something like an electron.
Regarding the fact that neutrinos are produced in beta decay, the down quark can be considered a composite particle, so it has orbital momentum and its energy and spin are thought to correspond to those of the neutrino, but further consideration is required.

![image_ch6_fig6-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig6-2.png)

Fig. 6-2 Beta decay

## 7. Review of neutrino model
In Chapter 5, I explained that the neutrino is represented by oscillation mode 2, which is the resultant rotation vector of three-axis rotation vectors that oscillate in phase. However, the neutrino has a spin of 1/2 and should have two rotation components.
It is the rotating vector pair that has spin 1/2. It is thought that it cannot exist alone, and even if it could exist alone, it would precess, which means that electromagnetic interaction with the photon would occur, which does not match the properties of the neutrino.

Oscillation mode 4 is the same as a rotating vector pair, and oscillation and rotation are basically the same phenomenon. 
Therefore, if the phase that is shifted by 90 degrees in oscillation mode 4 is matched, the length of the composite rotating vector oscillates as in oscillation mode 2 (this will be called oscillation mode 4-1).
Furthermore, if the phase is slightly shifted rather than perfectly matched, it will rotate little by little while oscillating. This is thought to represent neutrino oscillation, but further consideration is needed.

![image_ch6_fig7-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch6_fig7-1.png)

Fig. 7-1 Reviewed neutrino model

(Try elementary_particles.py for Fig 7-1.)

## 8. Review of precession and spin
It was a mistake to think that the infinitesimal precession described in Chapter 4 would lead to a 45 degree precession.
However, the 45 degree precession due to the spin 1/2 of fermions arises naturally from the properties of rotation and space-time (orthogonality and symmetry).
And as I said in Chapter 4, in Minkowski space photons and electrons always interact at an angle of 45 degrees. This is the mechanism behind the principle of the constancy of the speed of light.

## 9. Conclusion
* When a rotation vector is rotated in a direction perpendicular to its axis, the axis precesses at an angle of 45 degrees due to the interaction between the rotation of the rotation vector itself and the rotation in the perpendicular direction.
* The time axis in four-dimensional space (Minkowski space) is perpendicular to the spatial axis, so the time axis also precesses at a 45 degree angle.
* A state in which only the rotation of the rotation vector itself (single rotation) is spin 1, and a state in which a double rotation component in an orthogonal direction is added (rotation vector pair) is spin 1/2.
* Elementary particles with electric charge, such as electrons and quarks, are composed of rotating vector pairs, and the number of rotating vector pairs indicates the magnitude of the electric charge.
* Charged elementary particles such as electrons and quarks have spin 1/2, which causes their space-time axis to be tilted at a 45 degree angle in Minkowski space with respect to the space-time axis of a spin 1 photon, so they can only interact with a spin 1 photon at a 45 degree angle.
* In Minkowski space, angles indicate speed. Therefore, the speed of a photon interacting with an electron or a quark is always constant at 45 degrees, and therefore the speed of light is constant.


# Chapter - 7. Rotation, Spin and Mass

What is mass?

Watch my video for overview!

[(https://youtu.be/9iO9gvuThDo)](https://youtu.be/9iO9gvuThDo)

## 1. Introduction
In Chapter 6, I explained that fermions can be represented by a rotating vector pair. 

A rotating vector pair is a double rotation, and the idea of  double rotation comes from the ½-fold rotation symmetry and the path integral invented by Feynman, as explained in Chapter 3.

Now that we understand that fermions can be explained by a combination of rotating vector pairs, we will consider the relationship between rotating vector pairs and path integrals, and consider the Planck constant and mass.

## 2. Projection of rotation vector
In the previous chapters, I have explained that a photon can be represented by a rotating vector (light-arrow), and a fermion can be represented by a rotating vector pair, which is a pair of a rotating vector in the direction of the space axis and a rotating vector in the direction of the time axis.

When we represent a photon as a rotating vector, it may seem as if the photon is moving in a specific, fixed direction. 

However as explained in Chapter 2, in this theory the direction of the rotating vector is not fixed; rather, it rotates (Chapter 3) or changes direction randomly (Chapter 5), and spreads out spherically in Minkowski space (light-sphere).

Then, it is projected onto the entire spatial axis of the observer. It randomly interacts with the observer (fermion). 
(And since fermions have spin 1/2, they only interact at a 45 degree angle in Minkowski space, i.e., at the speed of light c, so the speed of light remains constant (Chapter 6).)

When the rotation vector of a photon is projected onto the observer's spatial axis, the phase of the rotation vector is projected according to its gradient. 

This is because in Minkowski space, the phase θ = tan-1 (x/t), where x/t is the gradient. 

![image_ch7_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig2-1.png)

Fig. 2-1 Projection of rotation vector

And because the gradient in Minkowski space indicates the speed, rotation vectors of any direction are projected onto the spatial axis at the same time as seen by the observer. This gives photons the properties of waves that propagate in space.

![image_ch7_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig2-2.png)

Fig. 2-2 Detail of the projection of rotation vector

In the case of fermions, as explained in Chapter 3, due to the double rotation as shown in the figure, the phase of the rotation vector is proportional to the square of the projected position x (and the fact that the phase is proportional to the square of x is consistent with the path integral formula, which is equivalent to the Schrödinger wave function).

![image_ch7_fig2-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig2-3.png)

Fig. 2-3 Projection of rotation vector in chapter 3

## 3. Projection of rotation vector pair
Now that we know that fermions can be represented as rotating vector pairs, as explained in Chapter 6, let us try to reconcile the double rotation mentioned above with the case of rotating vector pairs.

In a rotation vector pair, the two rotation vectors influence each other and precess at an angle of 45 degrees. Therefore, when considering the projection of the rotation vector (=light-arrow) of the rotation vector pair in the spatial axis direction, it is sufficient to tilt the phase rotation plane by 45 degrees.

![image_ch7_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig3-1.png)

Fig. 3-1 Phase surface of rotation vector pair

This rotating vector is projected onto the observer's space plane according to its phase, just like with photons.

At this time, because the phase surface is tilted by 45 degrees, the rotational speed of the rotating vector becomes √2 times as shown in the figure when it is projected onto the space plane (this is because the length of the wavelength, when the rotation is considered as a oscillation, appears shorter when projected).

![image_ch7_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig3-2.png)

ig. 3-2 Projected rotation vector speed

This projection is then rotated relative to the observer's time axis because it is affected by the precession rotation. The precession rotation speed is the resultant rotation vector of the vector pair, which is also multiplied by √2.

Therefore, both phases change in the same way, and the phase is set to θ.

![image_ch7_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig3-3.png)

Fig. 3-3 Precession rotation speed of rotation vector pair


The spatial rotation vector of the rotation vector pair is projected as shown in the figure.

![image_ch7_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig3-4.png)

Fig. 3-4 Projection of rotation vector pair

In Chapter 3, the rotation plane of the fermion phase was not tilted, so it was difficult to find physical meaning in the relationship with the projected value and the path integral (proportional to the square of x), but this became clear when projecting the rotation vector pair.

Also, the above projection only shows a projection in one direction, and if projected on the entire xy plane, it will look like the figure. 

What is interesting here is that in the case of photons, projections appear radially from the central axis (z axis = time axis), but in the case of fermions, no phase projection appears inside the precession circle. This is thought to be related to Fermi's exclusion principle.

![image_ch7_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig3-5.png)

Fig. 3-5 Projection path of rotation vector pair

(Try projection_rotation_vector_pair.py and projection_rotation_vector_pair_multi.py for Fig 3-4.)

## 4. Projection of rotation vector pairs, and mass
In the previous section, we were able to clarify the physical meaning of the relationship between the projection of the rotating vector pair representing the fermion and the path integral. 

Next, we will consider the relationship between the projection of the rotating vector pair and the path integral formula. 

The propagator formula for the path integral of a free particle is as follows.

![image_ch7_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-1.png)

Fig. 4-1 Propagator formula for the path integral

The coefficients in this equation represent the spread of the wave function over time, the exponents represent the action, and the imaginary power of e represents the rotation from Euler's formula.

![image_ch7_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-2.png)

Fig. 4-2 Explanation of propagator formula

Based on this, the equation introduced in Chapter 3, written by Brian Cox and Jeff Forshaw in the book THE QUANTUM UNIVERSE (and why anything that can happen, does) rewrites the relationship between the change in phase of the probability amplitude (number of rotations) and distance.

![image_ch7_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-3.png)

Fig. 4-3 Brian Cox and Jeff Forshaw formula

The change in phase is proportional to x2/t, and if the change in m is large, the change in phase is also m times larger, so the phases at distant positions tend to cancel each other out more easily, and the probability amplitude tends to become smaller. 

This equation means that elementary particles are difficult to find at distant positions and difficult to move, which corresponds to the fact in classical physics that the heavier the mass, the harder it is to move.

![image_ch7_fig4-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-4.png)

Fig. 4-4 Detail of Brian Cox and Jeff Forshaw formula

![image_ch7_fig4-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-5.png)

Fig. 4-5 Path integral

Next, looking at the projection relationship of the rotating vector pair, the greater the rotation speed (frequency) of the rotating vector pair, the larger the projected phase. 

Since this is the same as the relationship between mass (m) and phase described above, the rotation speed of the rotating vector pair and mass (m) can be considered to be the same. 

In other words, mass is the rotation speed of the rotating vector pair itself (Here, the Planck constant can be considered as a proportional constant for the rotation speed and mass of the rotating vector pair, but further consideration is needed.).

![image_ch7_fig4-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-6.png)

Fig. 4-6 Relation between the projection of rotation vector pair and Brian Cox and Jeff Forshaw formula

And when considering this theory (Light-sphere in Minkowski space), the rotation of the coordinate system indicates acceleration. Since mass generates gravity, it can be considered the source of gravity, and is consistent with the equivalence principle of general relativity (gravity = acceleration).

![image_ch7_fig4-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch7_fig4-7.png)

Fig. 4-7 Rotation in Minkowski space

Note that the projection of the rotation vector pair described in the previous section represents a relationship that does not take into account temporal diffusion (before temporal diffusion is applied), and can therefore be related to a path integral that does not take into account temporal diffusion.
 (In this theory, the time diffusion is considered to be the light-sphere expanding according to the Huygens-Fresnel principle as explained in Chapter 2, but further consideration is required.)

## 5. Conclusion
* The projection of the rotation vector pair can be related to a path integral that does not take into account the diffusion in time.
* Looking at the projection relationship of a rotating vector pair, the greater the rotation speed (frequency) of the rotating vector pair, the greater the projected phase.
* Therefore, the rotation speed (frequency) of the rotating vector pair and the mass (m) included in the path integral equation can be considered to be equivalent.

# Chapter - 8. Rotation and Space-time

What is space-time?

Watch my video for overview!

[(https://youtu.be/gylxe47y5BI)](https://youtu.be/gylxe47y5BI)

## 1. Introduction
In Chapter 2, we discussed how a Light-sphere spreads spherically through Minkowski space, which is four-dimensional space-time, like waves spreading on the surface of water.
We also discussed how this four-dimensional Light-sphere projected onto three dimensions is the three-dimensional world we can recognize. 
How does a Light-arrow spread into four-dimensional space as a Light-sphere? And how is it projected into three dimensions? 
In this chapter, we will consider Light-spheres and space-time.

## 2. Huygens-Fresnel principle and rotation vector
The Huygens-Fresnel principle is the theory that elementary waves, which are small circular (spherical in 3D) waves, overlap to form a wavefront, and can explain phenomena such as light refraction and diffraction.
Elementary waves generated at each point on a wavefront form the next wavefront, and the elementary waves of that wavefront form the next wavefront, and so on.

![image_ch8_fig2-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig2-1.png)

Fig. 2-1 Huygens-Fresnel principle

(Try wave_simulation_cell.py at https://github.com/marukatsutech/wave_simulation for Fig 2-1.)

On the other hand, what has been explained in this theory is that photons and fermions are rotating vectors that change direction randomly.
 How can we reconcile elementary waves propagating in a medium with vectors that move randomly?
 If the rotating vector were to disperse and spread in the same way that elementary waves disperse and spread, the problem of wave function collapse would arise.

![image_ch8_fig2-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig2-2.png)

Fig. 2-2 Do rotation vectors spread apart?

## 3. Dimensions and Projections
In this theory, the Light-sphere spreads in a four-dimensional space, which is then projected into three dimensions. 
What does it mean to project? 
We can only perceive three-dimensional space (plus time), so we cannot perceive four-dimensional space as it is. 
It is the same as if the inhabitants of a two-dimensional world could not perceive three dimensions. 
However, it can be indirectly recognized by cross sections and projections. 

For example, when a sphere passes by another in a two-dimensional world, the inhabitants of the two-dimensional world perceive the circle as the cross section of the sphere. 
The sphere can also be recognized by projecting it so that the shadow of the light is reflected on it.

![image_ch8_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig3-1.png)

Fig. 3-1 cross sections and shadow

Four-dimensional objects can also be recognized in three dimensions as cross sections and projections, and the following figure shows a projection of a tesseract(4D hypercube) into three dimensions.

![image_ch8_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig3-2.png)

Fig. 3-2 Tesseract(4D hypercube)

(Try hypercube.py at https://github.com/marukatsutech/hypercube for Fig 3-2.)

## 4. Minkowski Space and Projection
Next, let us consider how the Light-sphere is projected into three dimensions. 
In ordinary Minkowski space, there are proper time and proper distance, which are invariant properties under Lorentz transformation, and they are expressed by hyperbolas. (In the case of x, y, and c-t three axes, it is a hyperboloid).
In the Light-sphere version of Minkowski space (hereafter called Light-sphere space), both the proper time and the proper distance are expressed by circles (spheres), and they overlap. 

![image_ch8_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig4-1.png)

Fig. 4-1 Proper time and proper distance in Minkowski space and Light-sphere space

The Poincaré disk and the Klein disk are examples of the projection relationship between this hyperbola (hyperboloid) and a circle (sphere). 
These are related to hyperbolic geometry, and the circumferences of the disks represents infinity. 
When expressing the relationship between the hyperboloid and the disk, they are related through a semicircle (hemisphere) as shown in the following figure. 

![image_ch8_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig4-2.png)

Fig. 4-2 Relation between Poincaré disk, Klein disk and hyperboloid

(Try poincare_klein_disk.py at https://github.com/marukatsutech/poincare_klein_disk for Fig 4-2.)

The relationship in this figure and the projection relationship in Light-sphere space are similarly related to the distance from position zero to infinity on the circumference. 

![image_ch8_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig4-3.png)

Fig. 4-3 Relation between Light-sphere , Poincaré disk, Klein disk and hyperboloid

Since the upper side of the light cone in Minkowski space represents the future and the lower side represents the past, the upper hemisphere of the Light-sphere represents the future and the lower hemisphere represents the past.

![image_ch8_fig4-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig4-4.png)

Fig. 4-4 Relation between Minkowski space and Light-sphere space

## 5. Rotation and space-time
Let's now move away from the issue of projection for a moment and further compare Minkowski space and Light-sphere space. 
As mentioned above, the hyperbola in Minkowski space represents proper time and proper distance. This hyperbola can be expressed by the following equation. 
Here, as the coefficients a or b approach zero, the hyperbola approaches a straight line, which is the trajectory of light. 

![image_ch8_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-1.png)

Fig. 5-1 hyperbola in Minkowski space

(Try hyperbola.py at for Fig 5-1.)

From this, light can be considered to be the same as proper time and proper distance.
 If this is the case, and light in Light-sphere space is also considered to be the same as proper time and proper distance, the trajectory of light should be considered to be circular rather than radial. 

![image_ch8_fig5-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-2.png)

Fig. 5-2 Trajectory of light in Minkowski space and Light-sphere space

Now, let's consider that something that rotates is a photon. Here, we call this space, which is neither Minkowski space nor Light-sphere space, R-space. 
In this space, photons continue to rotate until they interact with a fermion. We also consider fermions to be something that rotates just like photons. However, in the case of fermions, we consider them to rotate doubly.
We also consider that photons and fermions interact when their rotation phases match.

![image_ch8_fig5-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-3.png)

Fig. 5-3 How a photon and a fermion interact in R-space

First, let’s consider photons. 
If you draw a diagram of something that continues to rotate, the trajectories will overlap, so we will shift the circle along the axis of rotation for each rotation.
In this case, if the rotation speed is large, the shift interval is narrowed according to the ratio of the rotation speed. 

![image_ch8_fig5-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-4.png)

Fig. 5-4 Photons in R-space

This is to make the number of rotations correspond to the frequency of the photon, and photons travel at a constant speed regardless of the magnitude of their frequency.
It is easier to understand this if you think of it as a helix rather than a line of circles, but for the purposes of the following discussion we will continue to explain it as a circle.

![image_ch8_fig5-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-5.png)

Fig. 5-5 Frequency of photons in R-space

If these photons are lined up, a one-dimensional coordinate axis is created with the length of the axis of rotation as one scale. 
Note that, for ease of explanation, the diagram assumes that the rotational speed of light is a minimum, i.e. one rotation per arrow.
Next, a certain rotation is set as the origin (the circle where the rotation count starts), and the size of the circle is set to a radius the same as the distance from the origin. 
Then, it is possible to draw a diagram that resembles a light cone in Minkowski space.

The origin is the current rotation, the rotation above the origin is the future, and the circle below the origin is the past.

![image_ch8_fig5-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-6.png)

Fig. 5-6 Future and past in R-space

If you look at this diagram from the direction of the rotation axis, it becomes concentric circles, like a Light-sphere space.
 In Light-sphere space, the upper half of the concentric circles represents the future, and the lower half represents the past, but in this diagram (= R- space), the front of the display surface represents the future, and the back represents the past.

![image_ch8_fig5-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-7.png)

Fig. 5-7 R-space and Light sphere space

Next, let's consider fermions. 
Fermions are double rotated, and as explained in Chapter 6 and 7, two orthogonal rotation vectors form a pair. This causes them to precess.
Let's consider the two rotation vectors to be the same as a photon for now.
 If we consider the photon arrow as a rotation vector, the precessional rotation is the combination of the two rotation vectors, so the precessional rotation speed is √2 times that of the photon.

![image_ch8_fig5-8](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-8.png)

Fig. 5-8 Fermions in R-space

Similar to the rule that determines the length of the photon arrow to be constant, the shift interval is narrowed when the rotation speed is large. 
Because the rotation speed is √2 times that of the photon, the shift interval (length of the arrow) is narrowed by √2. 
Therefore, while the length of the arrow as a rotation vector is √2 times that of the photon, the scale in R-space is 1/√2 of the photon. 

![image_ch8_fig5-9](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-9.png)

Fig. 5-9 Relation between photons and fermions in R-space

The radius of the circle is also 1/√2 of the photon radius. This can be illustrated as follows.

![image_ch8_fig5-10](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-10.png)

Fig. 5-10 Photons and fermions in R-space

The circle of light expands according to the rotation number n, and the circle of the fermion expands in proportion to the rotation number n/√2. 
When this relationship is applied to the Light-sphere space, they intersect as shown in the figure. 
If the line connecting the intersection point and the center of the photon and fermion circles is taken as the phase, the phase difference (angle) is 45 degrees. 

![image_ch8_fig5-11](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-11.png)

Fig. 5-11 How a photon and  a fermion spread in Light-sphere space

This relationship where the photon circle and the fermion circle intersect is the same as the relationship when a photon reaches a fermion that is stationary (with zero relative velocity) with respect to the light source in Light-sphere space or Minkowski space.

![image_ch8_fig5-12](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-12.png)

Fig. 5-12 How a photon and  a fermion spread in Light-sphere space or Minkowski space.

However, the expansion of the radius for each rotation of the photon and fermion circles is introduced for convenience of illustration so that the rotation trajectories do not overlap, and the radius is not actually expanding.
 In R-space, the intersection in Light-sphere space or Minkowski space corresponds to the rotation phase being aligned. 
Since it is difficult to understand with a circle, if we think of R-space as a helix and unwind the helix and represent it on a graph, it will look like the figure below.

![image_ch8_fig5-13](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-13.png)

Fig. 5-13 R-space with helix stype

The vertical axis corresponds to time (called R-time), and the horizontal axis represents the rotation phase. 
Since the precessing fermion rotates faster than light, the phase advances faster. Therefore, the slope becomes gentler.

![image_ch8_fig5-14](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-14.png)

Fig. 5-14 How a photon and  a fermion spread in R-space with helix style

If the photon and fermion have the same origin, their lines will not intersect.
 To make their lines intersect, you just need to shift the origin of one of them in the time axis or phase direction.
And the relationship will be the same whether you shift it in the time axis or phase direction.

![image_ch8_fig5-15](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-15.png)

Fig. 5-15 How a photon and  a fermion intersect in R-space with helix style

Then, the circle (helix) in R space is a circle in the Light-sphere space. 
The direction of the phase in R space is the Light-arrow, and the direction of the Light-arrow indicates the speed, so the relative speed * time is the relative distance, and so the phase difference * R-time indicates the relative distance.

![image_ch8_fig5-16](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-16.png)

Fig. 5-16 Relative distance in R-space

In the above discussion, we have considered R-space as a helix, but the degree of helix progress (corresponding to the pitch of a screw) has been introduced only for the convenience of illustration. 
So, what is meant by a helix that does not progress?
In the case of photons, they simply continue to rotate as shown in the figure. The arrows in the figure simply indicate the direction of rotation.

![image_ch8_fig5-17](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-17.png)

Fig. 5-17 Photons without progress

In the case of fermions, the rotations are paired and they precess. (The reason for precession will be explained in the next section.)
Therefore, the phase also moves as shown in the figure. 
The difference between the phase movement of the fermion and the phase rotation of the photon creates a relative phase difference like a helix.

![image_ch8_fig5-18](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig5-18.png)

Fig. 5-18 Photons and fermions without progress

## 6. Photons and fermions
For photons, it is the rotation in R-space that was explained in the previous section.
 However, up until now, we have been discussing the rotation axis in one direction in R-space, that is, one dimension (one degree of freedom), but our world is three-dimensional, so it should have three degrees of freedom.
Therefore, rotation in R-space is also given three degrees of freedom.
 The trajectories of the phases of the three orthogonal rotations are observed as being projected onto the entire three-dimensional space of the universe (they interact in this way). 

Therefore, it can be said that the combination of the three rotation components spans the entire three-dimensional space. 
This means that one rotation of a photon is equivalent to the entire space of the universe. 
This is why strange phenomena such as the double-slit experiment of photons occur. One photon (rotation with three degrees of freedom) spans the entire universe, and one photon passes through two slits at the same time.
And observation (interaction) is not performed at an infinitesimal position or time, but can only be observed (interacted) within a certain width (Δx, Δt).

Therefore, the number of rotations and phase of R-space are observed within a certain width. 
So it can be considered as a rotating vector that rotates while proceeding through continuous rotations, or it can be observed as a superposition of wave functions or the uncertainty principle.
The three degrees of freedom rotation vectors can be considered as a single resultant rotation vector. 
Therefore, when they interact with each other, they behave as a single rotation vector (one degree of freedom rotation). This is wave function collapse.

![image_ch8_fig6-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig6-1.png)

Fig. 6-1 Uncertainty principle

![image_ch8_fig6-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig6-2.png)

Fig. 6-2 Resultant vector

In Chapter 6, I explained that the rotation vector of the space axis and the rotation vector of the time axis form a pair, but in R-space, the rotation itself is time and space. 
We will consider this as follows.
A vector that precesses in R space is considered to be the same as a photon. 
The circle of rotation oscillates up and down when viewed in a certain phase.
 Oscillation can be considered as one aspect of the rotation.

![image_ch8_fig6-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig6-3.png)

Fig. 6-3 Precession, oscillation and rotation of fermions

This oscillation (rotation) corresponds to the rotation vector of the time axis of the rotation vector pair. 
The reason for this oscillation (rotation) is that fermions, like photons, have three rotational degrees of freedom, and these three orthogonal rotations affect each of the rotation planes.

![image_ch8_fig6-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig6-4.png)

Fig. 6-4 How fermions precess

However, the three orthogonal rotations are also the same for photons, but photons do not oscillate (precession) in the plane of rotation, but simply behave as a resultant vector of the three directions. 
This difference is thought to be due to the difference in the speed of rotation. 
When a certain rotation speed is exceeded, the rotations in the three directions affect each other, causing oscillation (precession) in the plane of rotation. 
This is the reason why pair creation and annihilation occur, and fermions are essentially the same as photons. And like photons, fermions obey the wave function and uncertainty principle, and phenomena such as the double slit experiment are observed.

## 7. What is space-time?
From the above considerations, we can say that space-time is produced by rotation. 
And since rotation can be expressed as a rotation vector, R-space is thought to be the same as the state vector of Hilbert space in quantum mechanics. 
And the idea that space-time is produced from rotations (= time) seems to be close to quantum gravity theory and holographic cosmology. 
Also, the precession of fermions seems to be equivalent to Penrose's spinor.
And we can say that R-space gives them a physical meaning (geometric model).

In R-space, there are only rotation and phase, and no parameter called size.
 Does space-time really have no size? 
It is a strange idea that a rotating circle represents the entire universe, but it is not strange if you consider that the density of the circumference (phase) is about the same as the number of elementary particles in the entire universe. 
(It is strange that photons generated by stars far away in the universe can reach our eyes without attenuation, and the fact that photons are both particles and waves is quite strange.)

However, since it is difficult to imagine a rotation without size, it must have some kind of extension. 
Since the energy of a photon is E = hν (ν is a frequency and an aspect of rotation), it is thought that R-space has an extension of at least the Planck length. 
And, just as the extension was given when relating R-space to the Light-sphere space, it may have an extension. 
It is thought that the universe exists as something that rotates at the Planck length gathers together like an atomic nucleus, and sometimes overlaps.

![image_ch8_fig7-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch8_fig7-1.png)

Fig. 7-1 R-space

## 8. Conclusions
* Our universe is made up of R-space with three orthogonal degrees of freedom of rotation.
* In R-space, the rotation speeds of photons and fermions differ due to the effect of precession of the fermion rotation.
* Fermions in R-space interact with photons in such a way that the speed of the fermion appears constant in normal space due to the difference in phase speed between them.
* In R-space, that rotation corresponds to time, and the circumference of the rotation (rotational phase difference x time) corresponds to the distance in normal space.
* Therefore, one rotation of each of the fermion and photon interacts in such a way that it is omnipresent throughout all space in normal space, so one rotation of each is equivalent to the entire space we observe.
* When the rotation speeds of the three rotational components of a quantum increase, the rotations of the three degrees of freedom affect each other, causing the planes of rotation to oscillate and causing each rotation to precess.
* Photons rotate slowly and do not precess, while fermions rotate quickly and precess.

We don't know what is rotating in R-space, but we think that the rotating energy itself forms space-time. 
What should we call this rotating something? 
Until the mid-19th century, scientists searched for a medium through which light could travel.
 The rotating something is a little different from the image of light rippling, but if one aspect of rotation is vibration, it could be thought of as a wave. 
Let's call this rotating something R-aether. 
R is for rotation :-)

# Chapter - 9. Rotation and Space-time

What is U(1) x SU(2) x SU(3) symmetry ?

Watch my video for overview!

[(https://youtu.be/B0nJmVNqZno)](https://youtu.be/B0nJmVNqZno)

## 1. Introduction
In previous chapters, we have considered that our universe is made up of R-space, with three orthogonal degrees of freedom for rotation.
 These three orthogonal degrees of freedom influence each other, and as the rotation speed increases, the plane of rotation vibrates, causing each axis of rotation to precess. 
Photons are considered to rotate slowly and not precess, while fermions are considered to rotate quickly and precess. 

In the Standard Model of quantum mechanics, photons are considered to have U(1) symmetry, leptons such as electrons have SU(2) symmetry, and hadrons such as protons have SU(3) symmetry. 
In this chapter, we compare my theory (hereafter referred to as R-space theory) with existing quantum mechanical symmetries and reconsider the nature of elementary particles discussed in Chapters 5 and 6.


## 2. Gauge symmetry
Symmetries include translational symmetry and rotational symmetry.
 Regarding these symmetries, Noether's law (Noether's theorem) states that "whenever there is continuous symmetry, there is a corresponding conserved quantity." 
This means that if an action is invariant under continuous transformations (i.e., symmetry), the quantity corresponding to that transformation is conserved.
Spatial translational symmetry corresponds to the law of conservation of momentum, time translational symmetry corresponds to the law of conservation of energy, and rotational symmetry corresponds to the law of conservation of angular momentum.

There are various types of symmetry, but the symmetry dealt with in the Standard Model of quantum mechanics is called gauge symmetry, and includes the following types:
U(1) symmetry: Conservation of electric charge
SU(2) symmetry: Conservation of weak isospin
SU(3) symmetry: Conservation of color charge
These symmetries are similar to rotational symmetries, but the object being rotated (transformed) is not an object (particle) in the classical physical sense, but a wave function.

## 3. U(1) symmetry and the photon as a rotating vector
Mathematically, U(1) is the “unitary group of degree 1,” consisting of complex numbers e^iθ with absolute value 1.
It is like a "circle of radius 1" centered at the origin on the complex plane, and U(1) symmetry means that the essence does not change even if the angle (phase) is rotated by θ on this circle. 
However, the object that undergoes this transformation is the wave function that describes electrons, etc., and it becomes the following equation.

![image_ch9_fig3-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-1.png)

Fig. 3-1 xxxxxxx

Using Euler's formula e^iθ=cosθ+isinθ, e^iθ can be expressed as the following matrix. 

![image_ch9_fig3-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-2.png)

Fig. 3-2 xxxxxxx

This matrix is ​​the same as the matrix that performs a rotational transformation in plane coordinates.
Transformation with U(1) symmetry involves rotating the phase of the wave function. 
Rotating the phase at all positions by the same amount does not change the observed physical quantity. 

This is because the radius (squared) of a wave function at each position indicates the quantum observation probability, and rotating the phase globally does not change the radius at each position. 
Because the observed physical quantity does not change when transformed (rotated) in this way, this is called symmetry (just like how a circle or sphere looks the same when rotated).

![image_ch9_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-3.png)

Fig. 3-3 xxxxxxx

Next, consider a state in which a local transformation—specifically, a rotation—has been applied, so that the rotating phase varies from point to point. 
For example, imagine that the spiral spacing of the wave function becomes narrower, as illustrated in the figure. 
In a wave function, the narrower the spiral spacing (that is, the larger the gradient of the phase), the faster the quantum motion represented by that wave function. 

![image_ch9_fig3-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-4.png)

Fig. 3-4 xxxxxxx

In other words, the quantum is accelerated, and the observable physical quantities change accordingly. 
To ensure that conservation laws are not violated, an electromagnetic potential (photons) must appear to compensate for this change.

![image_ch9_fig3-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig5-1.png)

Fig. 3-5 Probability wave

The familiar facts that accelerating electrons requires applying an electric field (i.e., supplying photons), and that synchrotron radiation is produced when the direction of an electron’s motion is bent (accelerated) by a magnetic field, both arise from the conservation laws associated with this U(1) symmetry.
The following video shows how a gradient phase change is applied to the wave function representing the quantum.

![image_ch9_fig3-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-6.png)

Fig. 3-6 xxxxxxx

(Try xxxxxxxxx at https://github.com/marukatsutech/poincare_klein_disk for Fig 3-6.)

In R-space theory, photons are considered to be rotation vectors with orthogonal x-, y-, and z-axis components (three degrees of freedom). 
In contrast, U(1) symmetry in the Standard Model is "Unitary group of degree 1," meaning rotations around one axis (one degree of freedom).
 Photons have a property called helicity, which allows them to rotate counterclockwise or clockwise around that axis. 

![image_ch9_fig3-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-7.png)

Fig. 3-7 xxxxxxx

Thus, the number of degrees of freedom for photons in R-space theory differs from that of U(1) symmetry in the Standard Model. 
However, because the rotation of the three coordinate components of a photon in R-space theory is a rotation vector, it can be considered to be combined into a rotation around a single axis, and is therefore considered to be the same as U(1) symmetry.

![image_ch9_fig3-8](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-8.png)

Fig. 3-8 xxxxxxx

The reason why photons in R-space theory have rotation components on three axes is that, as explained in Chapter 8, in R-space rotation itself is space-time, and three-dimensional space requires three rotations, i.e., three degrees of freedom.
 When the three degrees of freedom of a photon are observed, only one degree of freedom is observed as a composite vector.

![image_ch9_fig3-9](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig3-9.png)

Fig. 3-9 xxxxxxx


## 4. SU(2) symmetry and the fermion as a rotating vector pairs
Mathematically, SU(2) is the “special unitary group of degree 2,” consisting of 2×2 complex unitary matrices with determinant 1.
While U(1) is a "rotation on a circle," SU(2) is a symmetry similar to a complex "rotation on a sphere.
" However, a rotation on a sphere does not simply mean a rotation on the surface of the sphere; every spherical surface has an additional degree of rotational freedom. 
Since rotation (position) on a sphere is determined by two values, latitude and longitude, the sphere itself is two-dimensional, just like a plane. 

![image_ch9_fig4-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig4-1.png)

Fig. 4-1 xxxxxxx

In mathematics, an n-dimensional sphere is generally represented as S2. 
A "complex rotation on a sphere" is S3, which is like a sphere in four-dimensional space. 
While figures in four-dimensional space cannot be illustrated, four-dimensional figures can be illustrated by projecting them into three-dimensional space, just as a three-dimensional sphere can be projected as a shadow onto a two-dimensional surface. 
An example of this is the Hypercube (Tesseract), where the vertices of a cube are rotated as shown in the following video.

![image_ch9_fig4-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig4-2.png)

Fig. 4-2 xxxxxxx

In R-space theory, fermions, like photons, have rotation vectors with x-, y-, and z-axis components.
However, because the rotation speed of these rotation vectors is high, the orthogonal rotation vectors influence each other. 
As a result, the rotation plane of each axis oscillates, and each rotation axis undergoes precession. 
These precessing rotation vectors are called rotation vector pairs.

![image_ch9_fig4-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig4-3.png)

Fig. 4-3 xxxxxxx

There are four degrees of freedom, with the addition of the precessional rotation to the three-axis rotation vectors, i.e., three degrees of freedom. 
Therefore, the rotation vector pair is thought to conform to a symmetry similar to the "rotation of a complex sphere" represented by SU(2).
However, as mentioned in Section 2, SU(2) symmetry implies that in the Standard Model, the weak force is induced by the conservation of weak isospin, and electrons and neutrinos are converted to each other through the intervention of the W boson. 

Unfortunately, R-space theory lacks consideration of the weak force, which involves the conversion of elementary particle types.

![image_ch9_fig4-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig4-4.png)

Fig. 4-4 xxxxxxx

## 5. Reconsideration of rotation vector pairs
Before considering SU(2) symmetry in R-space theory, including the weak force, we reconsider the rotation vector pair.
Elementary particles have a quantum number called spin that behaves like angular momentum; gauge particles that transmit force, such as photons and bosons, have a spin of 1, while elementary particles that make up matter, such as electrons and quarks, have a spin of 1/2. 
Electrons also have a magnetic moment due to their spin.
In an electromagnet, a magnetic moment is generated when current (flow of charge) rotates (circularly moves). 

However, although electrons have an electric charge, it is not known how electrons, which are considered to be sizeless points, generate a magnetic moment (there is also a theory, such as superstring theory, that elementary particles are not sizeless points but extended strings).

![image_ch9_fig5-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-1.png)

Fig. 5-1 xxxxxxx

The magnetic moment arising from the electron’s spin has been confirmed experimentally by the Stern–Gerlach experiment. 
Curiously, although an electron (in practice, silver atoms are used in the experiment) behaves like a tiny magnet, its orientation is not “free to point anywhere.” 
Instead, only two outcomes are allowed relative to the direction of the applied magnetic field: “up” or “down.” 

![image_ch9_fig5-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-2.png)

Fig. 5-2 xxxxxxx

Furthermore, if an electron that has been measured to be spin‑up is measured again along the same vertical axis, it will again be observed as spin‑up.
 However, if that same spin‑up electron is measured along a horizontal magnetic‑field direction, the spin does not simply disappear; instead, it is observed to be pointing left or right with equal probability of 50%.

![image_ch9_fig5-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-3.png)

Fig. 5-3 xxxxxxx

In this way, the result of a spin measurement depends entirely on how the measurement is performed.  
Spin may seem like a quantity with no concrete physical reality, yet the magnetic fields produced by magnets in the real world ultimately originate from the spins of electrons. 
The transformations between the spin‑up and spin‑down states follow the symmetry of the group SU(2).
However, in the Standard Model of quantum mechanics, it is said that the spin direction can be changed by an SU(2) transformation, but the gauge particle that changes the spin direction is not a W boson, but a U(1) photon.

As explained in Chapter 6, spin in R-space theory is considered to result from the double rotation of a rotating vector pair. 
However, there are two issues with this.
First, the three axes (x, y, and z) cannot precess at a 45-degree angle while remaining orthogonal.
If two axes are orthogonal, as shown in the figure, they can precess while maintaining a 45-degree angle, but the precession angle of the remaining axis is 90 degrees, and the speed of light changes only along that axis.

![image_ch9_fig5-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-4.png)

Fig. 5-4 xxxxxxx

The other issue is that, while isotropy is required from the perspective of “Light speed constancy”, it must be anisotropic from the perspective of “spin”. 
As mentioned above, the magnetic moment due to electron spin can change depending on how it is observed. 
However, if it is observed to be pointing upward, subsequent observation of the magnetic moment in the up-down direction will again observe it as pointing upward. 
This suggests that electrons have some kind of anisotropy.

Therefore, we allow partial disruption of the orthogonal relationship between the three rotation axes. 
Also, up until now, we have considered the rotation of a rotation vector or a rotation vector pair as the rotation of a point with no size, but we will now consider the rotation vector as a rotation moment and take into account the size of the rotation (the radius of the rotation moment).
First, we create two unit circles on mutually orthogonal planes, with each circle centered on the other. 
This is called a Hopf link. 


![image_ch9_fig5-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-5.png)

Fig. 5-5 xxxxxxx

The rotation axes of these two circles are considered to be the x-axis and the y-axis rotation vectors in R-space theory, and they precess due to each other's influence, forming a rotation vector pair. 
The resultant rotation vector of this rotation vector pair and the z-axis rotation vector form a further Hopf link.
 In this case, the resultant rotation vector of the x-axis  and the y-axis rotation vectors is √2 times the x-axis and y-axis rotation vectors, because the x and y axes are orthogonal (Pythagoras' theorem). 
Therefore, to balance with the z-axis rotation vector, the radius of the circle of z-axis is set to √2 times the unit circle.

This new rotation vector pair model is called the Hopf link rotation vector pair model. 
The rotation vector pair of the x-axis and y-axis components is called the minor link, and the resultant rotation vector of the x-axis and y-axis components and the z-axis component is called the major link. 

![image_ch9_fig5-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-6.png)

Fig. 5-6 xxxxxxx

The combination of the rotation axes that make up the minor link and major link cannot be stabilized due to thermal vibration, and is constantly swapped. 
(As explained in the next section, the Hopf link expands and contracts like a spring, so the relationship between the major link and minor link is constantly swapped as the size of the link oscillates.)
In this Hopf link rotating vector pair model, although there is some disturbance in the orthogonal relationship between the x-axis component, y-axis component, and z-axis component, all axes precess at an angle of 45 degrees, so it is isotropic from the viewpoint of the constancy of the speed of light, but is anisotropic from the viewpoint of the magnetic moment because the radius of rotation of the Major link is large.

The Stern–Gerlach experiment using this Hopf link rotation vector pair model can be explained as follows:
In the absence of a magnetic field, the relationship between the major link and minor link is constantly swapped, but when a magnetic field is applied in the vertical direction, the major link aligns with the magnetic field. 
It is then pulled upward or downward depending on the direction of rotation (clockwise or counterclockwise). 

![image_ch9_fig5-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-7.png)

Fig. 5-7 xxxxxxx

The orientation of the major link is maintained unless an external force (measurement, electromagnetic radiation, etc.) is applied. 
Therefore, if a magnetic field is subsequently applied in the vertical direction and measurements are taken, the spin direction measured will be the same as the initial spin direction. 

![image_ch9_fig5-8](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-8.png)

Fig. 5-8 xxxxxxx

If a magnetic field is then applied in the horizontal direction and observations are made, an external force(a magnetic field) is applied, which disrupts the combination of rotation vectors and causes the major link to be reconstructed in the horizontal direction, so the spin is now observed in the left-right direction.

![image_ch9_fig5-9](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-9.png)

Fig. 5-9 xxxxxxx

If a magnetic field is then applied in the horizontal direction and observations are made, an external force(a magnetic field) is applied, which disrupts the combination of rotation vectors and causes the major link to be reconstructed in the horizontal direction, so the spin is now observed in the left-right direction.

![image_ch9_fig5-10](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-10.png)

Fig. 5-10 xxxxxxx

Additionally, the reason why particles are attracted to the upper or lower side depending on the direction of rotation (clockwise or counterclockwise) can be explained as follows. 
In R-space theory, interactions between charged particles occur when the phases of the elementary particles collide and invert, as described in Chapter 6. 
When two phase components (two rotation axis components) collide, the result is negative (-) * negative (-) = positive (+), and when three phase components (three rotation axis components) collide, the result is negative (-) * negative (-) * negative (-) = negative (-).

![image_ch9_fig5-11](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-11.png)

Fig. 5-11 xxxxxxx

Since the source of a magnetic field is electron spin, the state in which a magnetic field is applied to electrons can be said to be an interaction between electrons with aligned spin axes. 
If the rotational directions of the electron spins are the same, the spins cancel each other out, with one rotation axis component canceling out, resulting in an attractive force as each electron sees only two phase components of the other. 
If the rotational directions of the electron spins are opposite, the spins do not cancel out, resulting in a repulsive force as each electron sees two phase components of the other.

![image_ch9_fig5-12](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-12.png)

Fig. 5-12 xxxxxxx

Furthermore, since the rotation vector pair of the minor link that rotates on the circumference of the major link has two axes (two phase components), if we think of it as a rotating positive charge, then this is consistent with the Ampere force in classical physics, where currents flowing in the same direction exert an attractive force, and currents flowing in the opposite direction exert a repulsive force.
In addition, in a normal state, the direction of each electron spin changes randomly due to thermal vibration, etc., so three phase components are visible to each other and it is thought that a repulsive force is always present.

![image_ch9_fig5-13](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-13.png)

Fig. 5-13 xxxxxxx

It was explained that this Hopf link rotation vector pair model is composed of rotation vectors of three axes, but these three rotation axes are simply represented as basis vectors. 
Vectors that are not bases can be expressed as combinations of basis vectors. If we consider the Hopf link as rotation vectors in all directions, it becomes a Hopf fibration. 
A Hopf fibration is a decomposition of a three-dimensional sphere (S3) into "countless circles" and mapping them onto a two-dimensional sphere, and SU(2) symmetry, as mentioned above, is a "complex rotation of a sphere" and is equivalent to S3.

![image_ch9_fig5-14](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-14.png)

Fig. 5-14 xxxxxxx

In quantum mechanics, the quantum of a spin 1/2 particle such as an electron is represented by a two-component spinor (Pauli spinor). 
A two-component spinor is a two-dimensional complex vector composed of two complex numbers. 
If complex numbers are thought of as representing rotations, then a two-component spinor can be thought of as two rotations. 
In this new rotating vector pair model, it is composed of three rotation components (and their precessions). 

![image_ch9_fig5-15](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-15.png)

Fig. 5-15 xxxxxxx

(Try xxxxxxxxx at https://github.com/marukatsutech/poincare_klein_disk for Fig 5-15.)

However, if the rotating vector pair that makes up the minor link can only be observed as a resultant rotating vector, then the two rotation elements can be expressed as a spinor composed of two complex numbers.
As described above, the new rotating vector pair model, the Hopf link rotating vector pair model, appears to be consistent with the spin transformation (U(1) transformation) and SU(2) symmetry.

![image_ch9_fig5-16](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig5-16.png)

Fig. 5-16 xxxxxxx

## 6. Generation of elementary particles
Before considering the weak force, which involves the transformation of elementary particle types, we take one more step and consider the generations of elementary particles.
Electrons, neutrinos, and quarks have three pairs of elementary particles that have the same charge and spin but different masses, and these are called generations. 
In R-space theory, the generation of elementary particles could not be explained, but by incorporating the structure of a Hopf link into this rotation vector pair and giving it a size, it can be explained as follows.

![image_ch9_fig6-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig6-1.png)

Fig. 6-1 xxxxxxx

The Hopf link rotation vector pair model has a size, as mentioned in the previous section. 
We can think of this size as being expandable so that the combination of the minor link and major link can change. 
Furthermore, if we consider that space-time tends to suppress the size of the Hopf link rotation vector pair in order to stabilize it, then we can think of it as having a potential. 
If we think of rotation as vibration, then vibration under the potential will be quantized.

![image_ch9_fig6-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig6-2.png)

Fig. 6-2 xxxxxxx

The rotation of the minor link is considered to be a vibration, and there is a minimum period for this vibration (rotation) to be valid. 
For the major link to change size and for vibration to be stable along its circumference, the circumference must be an integer multiple of the width of the minor link's vibration period. 
(This is a relationship similar to the Bohr-de Broglie model, which describes an electron orbiting an atomic nucleus.)

![image_ch9_fig6-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig6-3.png)

Fig. 6-3 xxxxxxx

(Try xxxxxxxxx at https://github.com/marukatsutech/poincare_klein_disk for Fig 6-3.)

As the size of the major link increases, a force acts to return it to its original state.
If this force is considered proportional to the circumference of the major link, it can be thought of as a harmonic oscillator driven by the restoring force of a spring, and energy levels are quantized and generated. 
Since energy is equivalent to mass, this principle generates generations (mass differences) among elementary particles.

![image_ch9_fig6-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig6-4.png)

Fig. 6-4 xxxxxxx

Furthermore, in R-space theory, mass is considered to be rotation itself, as explained in Chapter 7.
The reason why there are only three generations is thought to be because there is a limit to the size of the major link (the spring's restoring force) (if the energy exceeds this, space-time cannot withstand it and it is transformed into a different combination of rotations = multiple elementary particles).

![image_ch9_fig6-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig6-5.png)

Fig. 6-5 xxxxxxx

## 7. Weak interactions
The weak interaction (weak force) appears in radioactive phenomena such as beta decay, where a W-boson is generated when a neutron changes into a proton, and this W-boson decays into an electron and an anti-electron neutrino. 
In the Standard Model, electrons and neutrinos have weak isospin, and electrons and anti-electron neutrinos are transformed through an SU(2)L transformation. (The "L" means left-handed; right-handed electrons do not have weak isospin and are therefore not affected by the weak interaction.) 

![image_ch9_fig7-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-1.png)

Fig. 7-1 xxxxxxx

The W-boson is generated due to the conservation laws resulting from this SU(2)L symmetry.
The formula for the SU(2)L transformation is as follows.
The SU(2)L transformation is similar to rotation, but the object being rotated is a doublet representing the electron and neutrino fields (wave functions), which is a complex vector with eight components expressed as complex numbers.
 The eight components are four components (up/down spin, particle/antiparticle) x two types of elementary particles (electrons and neutrinos).

![image_ch9_fig7-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-2.png)

Fig. 7-2 xxxxxxx

Electrons and neutrinos have very different physical quantities. 
Neutrinos have a very small mass, no electric charge, and do not interact electromagnetically. 
As a result, neutrinos hardly react with other matter, and pass through the Earth, the Sun, and even our own bodies without any effect. 
Also, because their mass is so small, this is similar to how photons pass through each other without interacting with each other (except for collisions between gamma rays). 
Also, because their mass is so small, they can travel at speeds close to the speed of light.

Neutrinos are something between photons and electrons. 
We consider them to be something between the photon model (rotation vector) described in Section 3 and the electron model (Hopf link rotation  vector pair) described in Sections 5 and 6.

![image_ch9_fig7-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-3.png)

Fig. 7-3 xxxxxxx

The precession angle of the rotating vector pair representing the electron is 45 degrees, but the precession angle of the neutrino is thought to be much smaller than 45 degrees. 
This is because, in R-space theory, the precession angle of the rotating vector is related to the arrival speed of gauge particles such as photons. 
As explained in previous chapters, the precession angle of the Hopf link rotating vector pair representing the electron is 45 degrees because the photon, a gauge particle relative to the electron, interacts at a 45-degree angle in Minkowski space, which is the projection of R-space. 

![image_ch9_fig7-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-4.png)

Fig. 7-4 xxxxxxx

The interaction at a 45-degree angle in Minkowski space means that the interaction occurs at the speed of light. 
The weak interaction only interacts over a very short distance. 
This means that the arrival speed of the W boson, a gauge particle, is slow, and it interacts at a small angle in Minkowski space, which means that the precession angle is small. 
(In the Standard Model, the W boson, a gauge particle of the weak force, is considered to have a short arrival distance due to its heavy mass.)

![image_ch9_fig7-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-5.png)

Fig. 7-5 xxxxxxx

Neutrinos also have a property known as neutrino oscillation. 
There are three generations of neutrinos: electron neutrinos, muon neutrinos, and tau neutrinos, and they change (oscillate) between these three generations. 
The three neutrino generations correspond to electrons, muons, and tau particles, respectively.
Taking this neutrino oscillation into account, the precession angle of neutrinos mentioned above can be considered to be changing (oscillating).

![image_ch9_fig7-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-6.png)

Fig. 7-6 xxxxxxx

Since the three axes cannot precess while remaining orthogonal, the precession angles of the three axes are changed to balance the equation.
From these facts, neutrinos can be considered to be in a state where their rotation vectors influence each other and precess, but they lack the rotational energy (rotational speed) to form a Hopf link rotation vector pair with a stable 45-degree precession.

![image_ch9_fig7-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-7.png)

Fig. 7-7 xxxxxxx

In beta decay, where the weak interaction is active, the W-boson decays into an electron and an anti-electron neutrino.
From the perspective of SU(2)L symmetry, the W-boson is a gauge particle necessary to maintain symmetry when an electron and an anti-electron neutrino transform, and is therefore the difference between the electron and the anti-electron neutrino. 
It is a set of rotation vectors that combine the rotational components of the electron neutrino, which is the antiparticle of the electron and the anti-electron neutrino. 

![image_ch9_fig7-8](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-8.png)

Fig. 7-8 xxxxxxx

Since the W-boson is a gauge particle with spin 1, it is thought that the precession is canceled out by the combined rotation of the electron and the electron neutrino. 
And because the W-boson is in an unstable state with the rotational components of two elementary particles, it decays into an electron and an anti-electron neutrino in a short time.

![image_ch9_fig7-9](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-9.png)

Fig. 7-9 xxxxxxx

Neutrinos come in generations such as electron neutrinos, muon neutrinos, and tau neutrinos, but the angle of precession of neutrinos oscillates, and no generation is stable. 
The particles that convert between them, such as electrons, muons, and tau particles, have their own generations, and are in discrete oscillating states due to the mechanism explained in the previous section. 
When these corresponding oscillating states are converted between them, they are observed as neutrino generations.

![image_ch9_fig7-10](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-10.png)

Fig. 7-10 xxxxxxx

So far, we have defined elementary particles by whether they precess or not, and the angle of precession. 
The precession angle of the photon, which is a gauge particle, is zero degrees (no precession). 
The precession angle of neutrinos oscillates at 45 degrees or less. 
The precession angle of charged particles such as electrons is 45 degrees.
 The precession angle of the W boson, which is a gauge particle and has a charge, is 45 degrees, but the apparent precession angle is canceled out by the precession component of the neutrino, making it zero degrees. 

From a symmetry perspective, then, there should be a particle with a precession angle of 45 degrees or more. 
This is thought to be the Z boson.
Z bosons are produced when neutrinos collide with other elementary particles, a process known as neutrino scattering. 
Z bosons are bosons with zero charge and spin 1. They have a heavy mass and a short lifetime, decaying quickly into particles and antiparticles such as electrons and positrons. 

![image_ch9_fig7-11](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-11.png)

Fig. 7-11 xxxxxxx

Z bosons are gauge particles that transmit forces like photons, but because they have mass, they also have spin, but the rotational components corresponding to the particle and antiparticle cancel each other out, so they are thought to behave like spin 1. 
Furthermore, because there is a range of Z boson masses (they decay into various particle and antiparticle pairs), the precession angle of Z bosons is thought to oscillate like that of neutrinos. 
Furthermore, particles with a precession angle of 90 degrees are also conceivable. These particles are thought to be axions, or dark matter.

![image_ch9_fig7-12](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig7-12.png)

Fig. 7-12 xxxxxxx

As described above, leptons and their gauge particles can be explained in terms of rotation vectors and their precession. 
SU(2) transformations are the rotation of complex vectors, which is the same as the rotation of a rotation vector. R-space theory is consistent with SU(2) symmetry and can also explain its mechanism (internal structure).
However, in the Standard Model, the weak interaction is more accurately explained by SU(2) L-symmetry, not SU(2). 
This L is left-handed, and this world distinguishes between right-handed and left-handed. This is called parity symmetry violation.
Next, we'll consider this parity symmetry violation.

## 8. Parity violation in weak interactions
SU(2)L symmetry only affects left-handed elementary particles. 
In the Standard Model, this is explained by the violation of parity symmetry.
This phenomenon manifests in weak interactions such as beta decay. 
Experiments have shown that electrons emitted during beta decay only fly in a specific direction (opposite to their spin). 
It was previously thought that symmetry in the laws of physics meant that physical phenomena would not change even if the left and right sides were swapped, but our world distinguishes between right-handed and left-handed.

In the Standard Model, elementary particles are represented by spinor-like complex vectors (two complex numbers). 
Complex numbers represent rotations, and since two rotations can be considered, one right-handed and one left-handed, there are four possible 2x2 combinations. 

![image_ch9_fig8-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig8-1.png)

Fig. 8-1 xxxxxxx

Applied to R-space theory, this results in a combination of a major link and a minor link. The minor link moves along the circumference of the major link. 
The rotation of the minor link is the resultant vector of orthogonal rotation vectors, so if the direction of the minor link's movement is opposite to that of the major link, the movement due to the minor link's rotation is canceled out.

![image_ch9_fig8-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig8-2.png)

Fig. 8-2 xxxxxxx

Therefore, it can be seen that four sets of symmetries are broken.
In the Standard Model, elementary particles are considered to be sizeless points, but in R-space theory, they have size and internal structure, so the cause of the symmetry breaking becomes clear.
As explained above, the lepton model in R-space theory is consistent with SU(2)L symmetry.

## 9. SU(3) and Hopf link rotation vector pairs
Mathematically, SU(3) is a "Special Unitary group of degree 3", a collection of 3x3 complex matrices with determinant 1 that are unitary matrices. 
If U(1) is a "circle" and SU(2) is a "rotation of a sphere", then SU(3) has an additional dimension and is a symmetry that "allows three states to be freely interchanged".
The object to be rotated (transformed) is a vector of three complex numbers called a color triplet, which corresponds to the color charge of a quark. 
As explained so far, complex numbers represent rotation, so this is three rotations.

![image_ch9_fig9-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig9-1.png)

Fig. 9-1 xxxxxxx

However, in R-space theory, there is no equivalent to color charge, and as explained in Chapters 5 and 6, protons and neutrons are composed of three quanta equivalent to electrons that share their respective rotation axes. 
This sharing corresponds to color confinement, and the quanta equivalent to electrons behave as up or down quarks depending on how they share the rotation axis.
Since R-space theory does not have color charge, before considering its relationship to SU(3), let us reconsider the models of protons and neutrons based on the idea of ​​the Hopf link rotation vector pair explained in Section 5.

In the quantum model explained in Chapter 6, three quanta have four (four-dimensional) rotation axes, including the time axis, as shown in the following figure. 
These rotation axes are then shared, and the shared axes become like electrons, resulting in color confinement.
In R-space theory, as explained in Chapter 8, time is the rotation of the rotation axes of the x-axis, y-axis, and z-axis components themselves that constitutes space-time, so the time axis is unnecessary. 

![image_ch9_fig9-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig9-2.png)

Fig. 9-2 xxxxxxx

And when we apply the Hopf link rotation vector pairs that we have explained so far, we get the following figure.

![image_ch9_fig9-3](https://github.com/marukatsutech/special_relativity/raw/main/image_ch6_fig6-1.png)

Fig. 9-3 Protons model

Quanta equivalent to three electrons provide the axes of each major link, and these three axes become electron-like (we will call this a shared quantum). 
The quantum that provided one axis as the major link of the shared quantum behaves as a down quark together with the shared quantum (since the shared quantum is a three-axis, it has a negative charge of 3/3, and the donating quantum is a two-axis, so it has a positive charge of 2/3, for a total negative charge of 1/3). 
The remaining two quanta each provide one axis to the shared quantum, so they become two-axis and behave as up quarks with a positive charge of +2/3. This shared quantum acts as the color confinement of the quark.

Next, regarding neutrons, in Chapter 6 I explained that the time axis is provided by the shared quantum between the two quanta, so that the shared quantum has an electric charge equivalent to two electrons, and that this charge makes it neutral (zero charge in UDD).
However, if there is no time axis (the essence of quanta and space-time is only the rotation of three axes), how should we think about this? This can be explained using SU(2)L symmetry, which was explained in Section 7.

![image_ch9_fig9-4](https://github.com/marukatsutech/special_relativity/raw/main/image_ch5_fig5-3.png)

Fig. 9-4 Neutrons model

When a neutron changes into a proton through beta decay, it emits a W-boson. 
As mentioned in Section 7, the W-boson has an electron and a neutrino component. This neutrino component is the second shared quantum.
 Neutrinos can be converted into electrons, and the rotation component corresponding to this neutrino behaves like an electron due to the rotation of the entire neutron.

![image_ch9_fig9-5](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig9-5.png)

Fig. 9-5 Neutrons model

As described above, quarks can be explained by the sharing of Hopf link rotation vector pairs and their rotation axes. 
The color charge (color triplet) of SU(3) symmetry indicates the three axes of the shared quantum, and the 3x3 complex matrix of the SU(3) transformation indicates the transformation of the three axes of the three quanta.

![image_ch9_fig9-6](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig9-6.png)

Fig. 9-6 xxxxxxx

This model (the shared electron model) also explains the strong force acting on quarks. 
As explained in Section 6 about generations, the size of the Hopf link of a quantum (in this case, the shared electron) expands and contracts like a spring. This corresponds to a gluon. 
The Hopf link is circular, and changes in size linearly, like the repulsive force of a spring. 

![image_ch9_fig9-7](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig9-7.png)

Fig. 9-7 xxxxxxx

As the energy increases (the rotation speed increases), the size of the link increases and the repulsive force trying to return to its original shape also increases linearly. 
This is consistent with the force exerted by the gluon (which is proportional to the distance, not inversely proportional to the square of the distance, as is the Coulomb force of electric charge). 
When the size of the Hopf link reaches its limit, like an overstretched spring breaking, the Hopf link can no longer maintain its structure and decays into a different elementary particle.

Furthermore, based on what has been explained so far, as the rotation speed (energy) of a rotating vector increases, the rotating vector precesses, the rotating vector pair, and the shared quantum combine into three quanta. 
This corresponds to photon → electron → proton or neutron, but this mechanism does not result in photon → electron → antiproton or antineutron. 
Furthermore, as explained in Section 8, electrons have restrictions on the combination of the rotation direction of the minor link and the rotation direction of the major link, breaking symmetry. 

Since the rotation direction cannot be reversed, antielectrons and antiprotons do not generally appear. 
Antiparticles appear as time reversals in Minkowski space, which is a projection of R-space. 
Therefore, there is little antimatter in this universe.

## 10. R-space theory and the Higgs field
The Higgs boson, also known as the God particle, is a particle that gives elementary particles mass. 
In the Standard Model, force-carrying gauge particles like photons, W bosons, and Z bosons are required to be massless. 
However, in reality, W and Z bosons possess mass, and so the Higgs field—and the Higgs boson itself, which is observed as a particle—were necessary to provide that mass. 
The Higgs boson was then discovered experimentally (though not by direct observation; rather, protons were collided, generating a Higgs boson with the resulting energy. 

![image_ch9_fig10-1](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig10-1.png)

Fig. 10-1 xxxxxxx

The pattern of elementary particles that decayed matched the theoretical decay of the Higgs boson). 
The Higgs field has viscosity, clinging to quanta that normally travel at the speed of light, creating resistance and slowing their movement, which is how mass is achieved. 
The magnitude of this viscosity varies from particle to particle. The Higgs field affects elementary particles differently, resulting in differences in their masses. 
However, it is unclear why the Higgs field affects each particle differently.

In R-space theory, as explained in Chapter 7, rotation itself is mass. 
And as explained in Chapter 8, when a photon interacts with a fermion, the phase (rotation component) in R-space is limited by the precession of the fermion's rotation vector, so the speed of light remains constant. 
As a result, the observation results are projected onto the space we perceive (Minkowski space) (equivalent to a Boost transformation). 
The phase of the projected rotation vector is proportional to the first power of the distance if the rotation vector does not precess, and proportional to the square of the distance if the rotation vector precesses. 

![image_ch9_fig10-2](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig10-2.png)

Fig. 10-2 xxxxxxx

Therefore, it is observed as a quantum wave like a wave function. 
In R-space theory, the only elementary particle that does not precess is the photon. Therefore, the W boson and Z boson, which precess, have mass.
And a high rotation speed increases the density of the phase.
 Because observation (interaction) operates within a certain width of spacetime, a high density weakens the influence of the interaction, resulting in less phase transformation. 
A small change in phase means a small change in distance and a large mass.

![image_ch9_fig10-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig10-3.png)

Fig. 10-3 xxxxxxx

Furthermore, quantum particles are observed probabilistically, and even heavy quanta can, although with a very small probability, travel far away in an instant. The R-space theory's explanation for this phenomenon is explained in Chapter 4.
As described above, the R-space theory's rotation vector and Hopf link rotation vector pair model can explain the U(1) x SU(2) L x SU(3) symmetry and the types and generations of elementary particles. 
The universe rotates naturally (stable) on three axes. As energy increases (the rotation speed increases), the rotation begins to deviate, the three axes twist, and a torus-like (donut-shaped) vortex forms. 

With even higher energy, the vortex becomes even more complex. 
The Higgs field is the force that suppresses this twisting (the force that tries to shorten the Hopf link). 
The Higgs particle is a particle formed when space, energized by proton collisions, twists and acquires rotational energy. 
The Higgs field is a property of space itself, and can be said to be a property of the R-aether in R-space theory.

![image_ch9_fig10-4](https://github.com/marukatsutech/special_relativity/blob/main/image_ch9_fig10-4.png)

Fig. 10-4 xxxxxxx

## 11. Conclusions
* All elementary particles are composed of a rotation vector, the R-aether rotating.
* A photon is a composite rotation vector of three rotation vectors: the x-, y-, and the z-axis component.
* If the rotation vector's rotation speed is high, the R-aether oscillates (expands and contracts), and begins an oscillatory precession. This is a neutrino.
* If the rotation speed is even higher, the precession angle becomes 45 degrees, and the rotation vector forms a stable Hopf link rotation vector pair. This is an electron.
* If the rotation speed is even higher, the R-aether stretches, the Hopf link widens, and the wave (rotation) quantization occurs due to the wave (rotation) relationship between the major link and minor link. This is the generation of elementary particles.
* If the rotation speed is even higher, the precession angle becomes greater than 45 degrees, resulting in an oscillatory precession. This is the Z boson. However, in order to maintain the stability (symmetry) of the R-ether, it can only exist in a state where it pairs with the rotational component of an antiparticle, canceling out the precession, and therefore behaves as a gauge particle with zero precession. However, because it is not stable, it decays after a short time.
* The W boson has a rotational component equivalent to that of an electron and neutrino, so it has charge and mass, but since the rotational components equivalent to that of an electron and neutrino cancel out, it behaves as a gauge particle.
* If the rotation speed is even faster, the precession is 90 degrees. This is axion = dark matter.
* If the rotation speed is even faster, the above precession does not hold (it cannot be more than 90 degrees), so a rotational vector equivalent to three more quanta forms the shared electron. These are the quarks that make up protons and neutrons.

R-space theory started from the assertion that "light is a sphere" in order to explain the principle of the constancy of the speed of light in the theory of relativity, but has since gone on to encompass the workings of elementary particles and space itself.
R-space theory can be considered an extension of Roger Penrose's twister theory, which states that space is created from light. 
Furthermore, explaining the types of elementary particles through combinations of three-axis rotation vectors and their precession and Hopf links is also consistent with the position of superstring theory and composite particle theory, which states that elementary particles have an internal structure.

Everything is just a different state of vortex (rotation). 
The universe is rotating.


We don't know what is rotating in R-space, but we think that the rotating energy itself forms space-time. 
What should we call this rotating something? 
Until the mid-19th century, scientists searched for a medium through which light could travel.
 The rotating something is a little different from the image of light rippling, but if one aspect of rotation is vibration, it could be thought of as a wave. 
Let's call this rotating something R-aether. 
R is for rotation :-)
