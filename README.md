# Note; refer main branch for latest version.
# Special relativity: Why is the speed of light constant?
# Chapter - 1. Light sphere

Light(Photon) is not a dot but a sphere that expands in Minkowski spacetime. 
* Light(Photon) is not a dot but a sphere.
* We can only observe our world with discretization (quantization)  just like moire pattern.
* That is why light speed does not change depending on the viewpoint of every observers.

Watch my video for more detail!  
[https://youtu.be/AwRgGn6AzzU  ](https://youtu.be/AwRgGn6AzzU)

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/master/image_special-relativity.png)

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

# Chapter - 2. The mechanism by which light spreading out as a sphere is observed at a single point.
## 1. Introduction
My argument in the last video (chapter - 1)was that light is a sphere spread out in Minkowski space(Fig 1-1). However, in reality, light is observed not as a surface but as a point. Regarding this, in the previous video, we only suggested that we could see what appeared to be light trajectories through the moiré patterns (interference fringes) created by concentric circles and stripes(Fig 1-2). This time, we will consider the mechanism by which light spreading out as a sphere is observed at a single point.

![image_fig1-1](https://github.com/marukatsutech/special_relativity/blob/master/image_fig1-1.png)

Fig. 1-1. Light spreading spherically in Minkowski space

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/master/image_special-relativity.png)

Fig. 1-2. Minkowski space and moiré pattern

Watch my video for overview!  
[https://youtu.be/aw-4OaHOQQU](https://youtu.be/aw-4OaHOQQU) 


## 2. Huygens-Fresnel principle in Minkowski space
Let's apply the Huygens-Fresnel principle to how waves propagate in Minkowski space.
Here, for simplicity, we will reduce the dimensions and consider a plane (two dimensions). First, when light is generated, it spreads out as a circle in a certain space (hereinafter referred to as light-speed-space). Here, for light, neither time nor space is fixed.
If this is observed from the standpoint of observer A,  the light seen from the observer will be as shown in the figure(Fig 2-1). (Although the space-time coordinates of observer B, who has a different relative speed than observer A, are tilted with respect to the space-time coordinates of A, the light spreads in a circle, so the light appears the same to both observers A and B.).

![image_fig2-1](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-1.png)

Fig. 2-1. Light circle seen from observers A and B

Next, we will look at how light spreads when viewed from observer A. Assuming that the length of each arrow is 1(Fig 2-2a), each arrow indicates the direction (velocity) in which light spreads. In Minkowski space, the slope of a straight line indicating the movement of an object indicates its speed, and a slope of 1 indicates the speed of light, so the speed of a light arrow that spreads out in a circular shape (hereinafter referred to as light-arrow) is equal to the slope of light-arrow from the standpoint of observer A. From then on, it should appear to progress from 0 to ± infinity.
In Minkowski space, the region exceeding the speed of light (slope = 1) is called a spacelike region, and is ignored because the law of causality does not hold, but here we will proceed with the idea without ignoring it and assuming that superluminal speed exists.

![image_fig2-2a](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-2a.png)

Fig. 2-2a. The light circle (light-arrow) seen by the observer

(Try light_arrows.py for Fig 2-2a.)

The arrival point of each light-arrow for observer A at time t=1 is plotted on the straight line at time t=1 as shown in Fig 2-2.b This is like a Mercator projection map that represents the spherical Earth on a flat surface.

![image_fig2-2b](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-2b.png)

Fig. 2-2b. How the light circle spreads as seen by the observer 

(Try light_arrows.py for Fig 2-2b.)


According to the Huygens-Fresnel principle, the wavefront at the next moment is formed by the overlap of circular secondary waves (elementary waves) from each point on the wavefront(Fig 2-3). 

![image_fig2-3](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-3.png)

Fig. 2-3. How secondary waves of light (elementary waves) spread in the speed-of-light space 

(Try light_arrows.py for Fig 2-3.)

Therefore, a wave spreads out in a circle from each point at time t = 1, and the circular wave is plotted in a straight line at time t = 2 in Minkowski space(Fig 2-4, 2-5). In this way, a wave that spreads circularly in light-speed-space will spread flatly in Minkowski space.

![image_fig2-4](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-4.png)

Fig. 2-4. How secondary waves (elementary waves) of light spread as seen from the observer in Minkowski space 
(Try light_arrows.py for Fig 2-4.)

![image_fig2-5](https://github.com/marukatsutech/special_relativity/blob/master/image_fig2-5.png)

Fig. 2-5. Waves spreading in a plane in Minkowski space 

(Try Huygens–Fresnel_Minkowski_space.py for Fig 2-5.)

## 3. Wave superposition and delta function
It turns out that a wave of light that spreads out in a circle spreads out in a plane in Minkowski space. Next, we need to converge the waves on this plane to a single point. The delta function(Fig 3-1, 3-2.) is a superposition of waves with an infinite frequency band.

![image_fig3-1_3-2](https://github.com/marukatsutech/special_relativity/blob/master/image_fig3-1_3-2.png)

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

![image_fig3-3](https://github.com/marukatsutech/special_relativity/blob/master/image_fig3-3.png)

Fig. 3-3. Superposition of waves with k(n) =1 /slope(n),　ωn= 1 

(Try light_speed.py for Fig 3-3.)

Furthermore, although the phase velocity is proportional to the slope of light-arrow, the fact that the angular frequency corresponding to the traveling velocity of the traveling wave (Equation 3-6) is constant is not worth removing the limit of light velocity.

y(t, x ) = f (x − vt)　…Equation 3-6

Now, let's assume that ω is proportional to the speed (= slope) of light-arrow. The wave equation in this case is as below.

y(n) = cos(2π(k(n)x - ω(n)t)) …Equation 3-7
 k(n) = 1 / slope(n) (= reciprocal of the slope of the arrow), ω(n) = slope(n) 

In this case, k(n) = 1 / slope(n), ω(n) = slope(n), so the phase velocity vp(n) = ω(n) / k(n) = slope(n) ** 2, which is the square of the slope of the light-arrow, and in this case However, as time progresses, the phase shifts and the peak collapses.

![image_fig3-4](https://github.com/marukatsutech/special_relativity/blob/master/image_fig3-4.png)

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

![image_equation3-11](https://github.com/marukatsutech/special_relativity/blob/master/image_equation3-11.png)

... Equation 3-11
 
Furthermore, since the phase velocity in this case is 

  ω(n) = k(n), vp(n) = ω(n) / k(n) = 1.
  
You can see a wave packet traveling at a phase velocity of 1 while maintaining the peak due to the superposition of waves.

![image_fig3-5](https://github.com/marukatsutech/special_relativity/blob/master/image_fig3-5.png)

Fig. 3-5. Superposition of waves with kn = slope(n),　ωn= slope(n)

(Try light_speed.py for Fig 3-5.)

Now, if we look at the wave equation from earlier,

y(n) = cos(2π(k(n)x - ω(nt))), k(n) = slope(n),　ω(n) = slope(n) ( = k)
  -> y = cos(2π(slope(n) * x - slope(n) * t))
  -> y = cos(2π* slope(n) * (x - t))  ...Equation 3-12

It is a collection of waves with wave number slope(n) times y = cos(2π * (x - t)), so there is no need to bring up group velocity.
Now, in the previous video, three waves were superposed, but let's increase the number of superpositions. 
The following video is a superposition of 100 waves with k(n) = ω(n) = slope(n) (n= 0.1, 0.2, 0.3…~10).

![image_fig3-5](https://github.com/marukatsutech/special_relativity/blob/master/image_fig3-6.png)

Fig. 3-6. Superposition of 100 waves with kn = slope(n),　ωn= slope(n)

(Try light_speed.py for Fig 3-6.)

The peak is clear compared to the superposition of three waves. It is still a superposition of 100 waves and two peaks appear, but if we further increase the number of superpositions and superimpose waves of infinite frequency (corresponding to the slope of light arrow from 0 to ± infinity), we get It should be in the form of a delta function with one peak.

Let us now consider the physical meaning of setting kn = slope(n), ωn = slope(n).
The reason for setting ωn = slope(n) is that we want the slope (=velocity) of the light-arrow to be equal to the traveling speed of the corresponding traveling wave. So what about kn = slope(n)?
Regarding this,in Minkowski space, x (distance) / t (time) = c (speed of light). If the speed of light increases by n times (ωn=slope(n)), the distance traveled (x) needs to increase by n times. This is thought to be because, assuming that the wavelength λ is constant, the distance traveled (x) cannot be multiplied by n unless the wave number is multiplied by n.
The above is the mechanism by which light waves spreading circularly in light-speed-space converge to a single point in Minkowski space.

#4. Conclusion
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

# Chapter - 3. What are quantum and spin? Bosons and fermions
## 1. Introduction
My argument from last time was that light-arrows spreads out in a circular (spherical) manner in light-speed-space, and from the observer's point of view (Minkowski spatial coordinate system) it spreads out (is projected) as a plane wave, and through superposition, it converges to a single point. 
That's what it meant. Light is one type of quantum called photon, and quantum and photon can be converted into each other through reactions such as pair annihilation and pair creation. If light can be represented as a circle (spherical) in Minkowski space, wouldn't it be possible to represent a quantum with mass like an electron as a light-arrow in light-speed-space?
This time, we will consider quanta that have mass.

Watch my video for overview!  
[https://youtu.be/agLXqUW5kyg](https://youtu.be/agLXqUW5kyg)

## 2. Bosons, fermions and spin
Quantums are classified into bosons, which transmit forces between quanta, and fermions, which make up matter. Photons are bosons that interact with electrons and transmit force; electrons are bosons. In addition, a quantum has a property called spin angular momentum (also simply called spin). The boson's spin is 1, and the fermion's spin is 1/2.

The current explanation of quantum spin is that although it is called spin, it does not mean that the quantum is actually spinning like a ball. However, doesn't the fact that the quantum spin has an angular momentum value lead to some kind of rotation?

![image_ch3_fig2-1](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig2-1.png)

Fig. 2-1. Spin of a photon

Then, what does the spin 1/2 of fermions such as electrons mean? Spin is related to rotational symmetry; a quantum with spin 1 has one-fold rotational symmetry, and a quantum with spin 1/2 has 1/2-fold rotational symmetry. Rotational symmetry refers to how many times a figure becomes indistinguishable during one rotation (360° rotation). 
If it is an equilateral triangle, if it is rotated 120 degrees, it will be in the same state as before the rotation, and it will be in the same state three times within one rotation (rotation 360 degrees), so it has three-fold rotational symmetry.

![image_ch3_fig2-2](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig2-2.png)

Fig. 2-2. Rotational symmetry of figures

Spin 1 means that the object will not be in the same state as before the rotation unless it is rotated once (360 degrees), so if it is spin 1/2, it will not return to its original shape unless it is rotated twice (720 degrees). It cannot be expressed in normal diagrams. 
If it returns to its original state after two revolutions, does spin 1/2 mean a rotation plus a rotation, such as a double rotation(Fig. 2-3), in which rotation is added to the circumference?

![image_ch3_fig2-3](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig2-3.png)

Fig. 2-3. Double rotation (circumferential rotation)

(Try double_rotation.py for Fig. 2-1.)

## 3. Path integral formulation and spin
Let's now change our perspective and consider the relationship with path integrals. 
The path integral formulation was devised by Richard P. Feynman, and is based on the idea that a quantum takes every possible path between its destination and the point it reaches, and integrates the probability amplitude of the quantum when it takes each path. 
It is said to be equivalent to the Schrödinger equation, which expresses the behavior of a quantum by calculating the probability of existence of a quantum at a point.

![image_ch3_fig3-1](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig3-1.png)

Fig. 3-1. Path integral formulation

I will not explain the formula for the path integral, but what it means is explained in the book THE QUANTUM UNIVERSE (and why anything that can happen, does)　by Brian Cox and Jeff Forshaw. 
According to that work, the change in the phase of the probability amplitude when passing through each path is expressed by the following equation (Equation 3-1), and the sum of the phases is the quantum at the observed position. Indicates the probability of existence.

![image_ch3_eq3-1](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_eq3-1.png)

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

![image_ch3_fig4-1](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig4-1.png)

Fig. 4-1a. and 4-1b. Projection of light circle

(Try projection_boson_fermion.py for Fig. 4-1.)

So far, we have only dealt with two dimensions (spatial axis x and time axis t for the observer) in order to simplify the discussion and make it possible to represent it in a plan view. Let's think about adding it.
When the inclination of the arrow of light is expressed as an angle θ from the time axis, the relationship between x and θ is x = tanθ (assuming that the length of the arrow of light = the radius of the light circle is 1). Furthermore, let's assume that the angle θ is from the added spatial axis (referred to as the y-axis) and that the arrow of light rotates like the precession of a top, as shown in Fig. 4-2. At that time, the projection of the arrow of light onto the x-axis is tanθ✕tanθ = x squared.

![image_ch3_fig4-2](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig4-2.png)

Fig. 4−2. Projection of light circle in 3 dimensions - 1

(Try projection_fermion_3d.py for Fig. 4-2.)

In addition, Fig. 4-2 is the same as the arrow of light rotating, just as the spinning top rotates sideways, and its axis of rotation also rotating, which can also be expressed as in Fig. 4-3. In Fig. 4-3, the tip of the arrow of light traces a twisted trajectory like a figure eight. This is thought to indicate the spin of the fermions.

![image_ch3_fig4-3](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig4-3.png)

Fig. 4−3. Projection of light circle in 3 dimensions - 2

(Try projection_fermion_3d_spin.py for Fig. 4-3.)

## 5. Conclusion
* Both bosons and fermions can be represented by light-arrows that spread out spherically in Minkowski space in this theory.
* The difference between bosons and fermions is that bosons have a rotational property on the time and space axes, and fermions also have another rotational property in the spatial direction.

![image_ch3_fig5-1](https://github.com/marukatsutech/special_relativity/blob/master/image_ch3_fig5-1.png)

Fig. 4-1. Spin of boson and fermion

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
