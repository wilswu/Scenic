
from scenic.core.vectors import *
from scenic.core.lazy_eval import DelayedArgument, valueInContext, needsLazyEvaluation
from scenic.core.distributions import Options, underlyingFunction

def test_distribution_method_encapsulation():
    vf = VectorField("Foo", lambda pos: 0)
    pt = vf.followFrom(Vector(0, 0), Options([1, 2]), steps=1)
    assert isinstance(pt, VectorMethodDistribution)
    assert pt.method is underlyingFunction(vf.followFrom)

def test_distribution_method_encapsulation_lazy():
    vf = VectorField("Foo", lambda pos: 0)
    da = DelayedArgument(set(), lambda context: Options([1, 2]))
    pt = vf.followFrom(Vector(0, 0), da, steps=1)
    assert isinstance(pt, DelayedArgument)
    evpt = valueInContext(pt, {})
    assert not needsLazyEvaluation(evpt)
    assert isinstance(evpt, VectorMethodDistribution)
    assert evpt.method is underlyingFunction(vf.followFrom)
