from estimator import *



LWE.primal_usvp(schemes.Kyber512)
r = LWE.estimate.rough(schemes.Kyber512)

# r = LWE.estimate(schemes.Kyber512)
