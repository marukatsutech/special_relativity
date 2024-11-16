# Special relativity: Why is the speed of light constant?
# Chapter - 1. Light sphere

Light(Photon) is not a dot but a sphere that expands in Minkowski spacetime. 
* Light(Photon) is not a dot but a sphere.
* We can only observe our world with discretization (quantization)  just like moire pattern.
* That is why light speed does not change depending on the viewpoint of every observers.

Watch my video for more detail!  
[https://youtu.be/AwRgGn6AzzU  ](https://youtu.be/AwRgGn6AzzU)

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/main/image_special-relativity.png)

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
My argument in the last video (chapter - 1)was that light is a sphere spread out in Minkowski space(Fig 1-1). However, in reality, light is observed not as a surface but as a point. Regarding this, in the previous video, I only suggested that we could see what appeared to be light trajectories through the moiré patterns (interference fringes) created by concentric circles and stripes(Fig 1-2). This time, we will consider the mechanism by which light spreading out as a sphere is observed at a single point.

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

# Chapter - 4. Relation between special relativity and quantum mechanics
# - wave function collapse and reconsidering of the quantum model -

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

![image_ch4_fig3-3](https://github.com/marukatsutech/special_relativity/blob/main/image_ch4_fig3-1.png)

Fig. 3-1 Random motion of Light-arrow

(Try photon_probability.py for Fig. 3-1.)

Since there are two phases here, in order to distinguish between them, we will call the phase of the light frequency energy the Light-phase, and the direction of the Light-arrow the Light-arrow-phase. The Light-arrow can be expressed as a rotating vector with the frequency (rotation speed) of light. And a photon is a rotating vector whose phase (Light-arrow-phase) changes randomly as it draws a Light-sphere.

By the way, so far I have not explained how the lower hemisphere of the Light-sphere is projected into space. Regarding the Light-arrow oriented in the lower hemisphere, you may feel that there is no projection destination in the direction of the arrow (it is projected in the direction of negative time). This can be explained from the observer's position (coordinates) with respect to the light-sphere.
When viewed from the observer's coordinates, the slope of the light-arrow (= position / time) indicates the speed. The slope of the Light-arrow in the third quadrant is space (minus) / time (minus) = velocity plus, and the Light-arrow is projected to the first quadrant side. The slope of the light arrow in the fourth quadrant is space (plus) / time (minus) = velocity minus, and the light arrow will be projected toward the second quadrant.

Next, consider the interference of probability waves. If we assume that one photon is composed of multiple light-arrows and that the light-arrows interfere with each other, we can easily explain interference. However, the randomly scattered light-arrows need to come together at the moment they are observed, and the same problem as wave function collapse remains. Considering the  of wave function　collapse, it is easier to explain Light-arrow in one form.

A case in which one object is observed to interfere is a case in which the objects move around at high speed.
For example, let's put an ant in a box with grids and observe in which grid it can be found (assuming that this ant can move around at high speed). If ants do not have a preference for squares, such as preferring the corners of a box, the probability of finding an ant in any square is equal. Then, place food (sugar, etc.) and obstacles in some squares. This results in a bias in the frequency of the directions in which ants pass depending on the grid.

Next, randomly select a square and catch an ant with tweezers. The direction of the opening of the tweezers must be kept constant. Also, if the opening of the tweezers do not open wider than the width of the ant, the ant can be caught only if the direction of the opening of the tweezers matches the direction in which the ant passes by. The more frequently the direction in which an ant passes matches the direction of the tweezers' opening, the higher the probability of catching an ant (Fig. 3-2).
In this case, one object causes interference and probabilistic observation results can be obtained(an ant is a photon, a tweezers is a fermion).

If we consider that a photon is something whose phase (Light-arrow-phase) changes randomly and rapidly, as if one Light-arrow draws a Light-sphere, then one photon interferes like a wave. , it can also be explained that when observed, it converges to one (wave function collapse).
What is meant by "keep the direction of the tweezers in a constant direction" will be explained in Section 5.

Note that if you take a long-exposure photo of this one ant, you will see afterimages of multiple ants in each square. Some of the squares show the ants passing in the same direction, while others show them in different directions. The image taken with this long exposure corresponds to the probability wave of the wave function.

## 4. Reconsidering the fermion model from the perspective of probability
## 5. Relation between quantum interactions and the principle of the constancy of the speed of light
## 6. Conclusion
