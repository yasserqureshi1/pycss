# pycss - Curvature Scale-Space

*Note: This is an adaption of [makokal's pycss repository](https://github.com/makokal/pycss) which was written in Python2*

## About

Curvature Scale Space is a shape descriptor for planar curves as was introduced by [Mokhtarian and Mackworth](https://ieeexplore.ieee.org/document/4767750). It is computed by convolving a path-based parametric representation of the curve with a Gaussian filter as the standard deviation of the Gaussian kernel is increased. Then zero-crossing points are extracted. Such a feature is found to be invariant under translation, rotation and uniform scaling.

Within this repository, four main curvature scale space representations can be developed:
1. Standard curvature scale space along with the CSS image
2. Visual curvature scale space - represents the CSS image in 1D
3. Eigenvector curvature scale space - generates eigenvector features 
4. Sliced Curvature Scale space (details found [here](https://ieeexplore.ieee.org/document/6766545))


## Installation

Install package using the command:
```
pip install setup.py
```

Install the dependencies using the command:
```
pip install -r requirements.txt
```


## Example Usage

```
>> from css import CurvatureScaleSpace
>> c = CurvatureScaleSpace()
>> cs = c.generate_css(curve, curve.shape[1], 0.01)
>> vcs = c.generate_visual_css(cs, 9)
```