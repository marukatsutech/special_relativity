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
My argument in the last video was that light is a sphere spread out in Minkowski space(Fig 1-1). However, in reality, light is observed not as a surface but as a point. Regarding this, in the previous video, we only suggested that we could see what appeared to be light trajectories through the moiré patterns (interference fringes) created by concentric circles and stripes(Fig 1-2). This time, we will consider the mechanism by which light spreading out as a sphere is observed at a single point.

![image_fig1-1](https://github.com/marukatsutech/special_relativity/blob/master/image_special-relativity.png)

Fig 1-1. Light spreading spherically in Minkowski space

![image_special_relativity](https://github.com/marukatsutech/special_relativity/blob/master/image_special-relativity.png)

Fig 1-2. Minkowski space and moiré pattern

Watch my video for overview!  
[https://youtu.be/AwRgGn6AzzU ](https://youtu.be/aw-4OaHOQQU) 


## 2. Huygens-Fresnel principle in Minkowski space
Let's apply the Huygens-Fresnel principle to how waves propagate in Minkowski space.
Here, for simplicity, we will reduce the dimensions and consider a plane (two dimensions). First, when light is generated, it spreads out as a circle in a certain space (hereinafter referred to as light-speed-space). Here, for light, neither time nor space is fixed.
If this is observed from the standpoint of observer A,  the light seen from the observer will be as shown in the figure(Fig 2-1). (Although the space-time coordinates of observer B, who has a different relative speed than observer A, are tilted with respect to the space-time coordinates of A, the light spreads in a circle, so the light appears the same to both observers A and B.).

Next, we will look at how light spreads when viewed from observer A. Assuming that the length of each arrow is 1(Fig 2-2), each arrow indicates the direction (velocity) in which light spreads. In Minkowski space, the slope of a straight line indicating the movement of an object indicates its speed, and a slope of 1 indicates the speed of light, so the speed of a light arrow that spreads out in a circular shape (hereinafter referred to as light-arrow) is equal to the slope of light-arrow from the standpoint of observer A. From then on, it should appear to progress from 0 to ± infinity.
In Minkowski space, the region exceeding the speed of light (slope = 1) is called a spacelike region, and is ignored because the law of causality does not hold, but here we will proceed with the idea without ignoring it and assuming that superluminal speed exists.

The arrival point of each light-arrow for observer A at time t=1 is plotted on the straight line at time t=1 as shown in Fig 2-2. This is like a Mercator projection map that represents the spherical Earth on a flat surface.

According to the Huygens-Fresnel principle, the wavefront at the next moment is formed by the overlap of circular secondary waves (elementary waves) from each point on the wavefront(Fig 2-3). Therefore, a wave spreads out in a circle from each point at time t = 1, and the circular wave is plotted in a straight line at time t = 2 in Minkowski space(Fig 2-3, 2-4). In this way, a wave that spreads circularly in light-speed-space will spread flatly in Minkowski space.

## 3. Wave superposition and delta function
It turns out that a wave of light that spreads out in a circle spreads out in a plane in Minkowski space. Next, we need to converge the waves on this plane to a single point. The delta function is a superposition of waves with an infinite frequency width.

Fortunately, as mentioned above, the slope (= velocity) of light-arrow, which is the element of the wave that spreads circularly in Minkowski space, appears from 0 to ± infinity speed from observer A, so this Let's use 0 to ± infinity to realize the superposition of waves with an infinite frequency width.
The equation of the wave in the video above is as follows(Equation 3-1). This is because in order to make it easier to see how circular light spreads out into a flat plane, the speed (=slope) of the light-arrow was made to match the advance of the phase.
y = cos(2π(kx -ωt))  ...Equation 3-1
 k (wave number) = 1 / slope (=reciprocal of the slope of the arrow of light)
 ω (angular frequency) = 1

 Note; The reason for multiplying by 2π is to adjust the phase so that when it advances by 1 in the x
         direction, the phase rotates once (one period of the wave).

The phase velocity vp (Phase velocity) of the wave expressed by the equation of 
y = cos(kx - ωt)) ...Equation 3-2 (k: wavenumber, ω: angular frequency)  is as follows.
vp = ω / k …Equation 3-3
Since the wave number k of the wave corresponding to each light-arrow is kn = 1 / slope(n), the phase velocity of each wave is as follows(Equation 3-4), and if the fundamental angular frequency ω is 1, then The speed of each wave is the slope of light-arrow = the speed of light (here, the speed of light is not constant, but ranges from 0 to ± infinity).
vp(n) = ω * slope(n)…Equation 3-4

Note; n or (n) is a suffix, and the variables with n or (n) hereafter represent the physical quantities of each light-arrow (n = 0 to ± infinity) and the corresponding wave.
Then, if we superpose these waves with wave numbers 0 to ±infinity (the equation is as follows), can we obtain a delta function?
y(n) = cos(2π(knx - ωnt))…Equation 3-5
  kn =1 / slope(n) (= reciprocal of the slope of the arrow of light), ω=1 
Unfortunately, since the phase velocities are different, as time progresses, the phases shift and the peak collapses.

Furthermore, although the phase velocity is proportional to the slope of light-arrow, the fact that the angular frequency corresponding to the traveling velocity of the traveling wave (Equation 3-6) is constant is not worth removing the limit of light velocity.
y(t, x ) = f (x − vt)　…Equation 3-6
Now, let's assume that ω is proportional to the speed (= slope) of light-arrow. The wave equation in this case is as below.
y(n) = cos(2π(knx - ωnt))…Equation 3-7
 kn = 1 / slope(n) (= reciprocal of the slope of the arrow), ω = slope(n) 

In this case, kn = 1 / slope(n), ωn = slope(n), so the phase velocity vp(n) = ωn / kn = slope(n) ** 2, which is the square of the slope of the light-arrow, and in this case However, as time progresses, the phase shifts and the peak collapses.

So, what is the combination of wave number k and angular frequency ω that does not shift the phase velocity? That is  the group velocities (vp;group velocities) are equal. Group velocity is the traveling speed of a wave packet created by superposition of waves, and can also be said to be the speed at which points with equal phase difference of waves travel, and its formula is as follows.
vg = dω / dk …Equation 3-8
When applied to this case, it is sufficient to satisfy the following conditions in which the standards ω and k are each 1, and in the simplest case, ωn = kn.
(ωn - 1) / (kn - 1) = constant ...Equation 3-9

When ωn = kn, the wave equation is as follows.
y(n) = cos(2π(knx - ωnt))
…Equation 3-10,
 kn = slope(n), ωn = slope(n) ( = k) 
Furthermore, since the phase velocity in this case is 
  ωn = kn, vp(n) = ωn / kn = 1.
You can see a wave packet traveling at a phase velocity of 1 while maintaining the peak due to the superposition of waves.

Now, if we look at the wave equation from earlier,
y(n) = cos(2π(knx - ωnt)), kn = slope(n),　ωn = slope(n) ( = k)
  -> y = cos(2π(slope(n) * x - slope(n) * t))
  -> y = cos(2π* slope(n) * (x - t))  ...Equation 3-11
 It is a collection of waves with wave number slope(n) times y = cos(2π * (x - t)), so there is no need to bring up group velocity.
Now, in the previous video, three waves were superposed, but let's increase the number of superpositions. The following video is a superposition of 100 waves with kn = ωn = slope(n) (n= 0,1, 0,2, 0,3…~10).

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




