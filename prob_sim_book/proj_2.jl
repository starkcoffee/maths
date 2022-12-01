using IterTools
using Lazy
using Statistics

# returns an array of all the vectors in {0,1}^n
function d_0_1(n)
  ranges = [ 0:1 for i in 1:n ]
  # cartesian product of ranges
  tuples = product(ranges...)
  # convert tuples to vectors
  return map(t -> collect(t), tuples)
end

function bound(D)
    m = size(D)[1]
    randomr() = rand(0:1, m)
    rs = Lazy.repeatedly(10_000, () -> randomr())
    mean([ D*r == zeros(m) for r in rs])
end

function exact_bound(D)
  m = size(D)[1]
  rs = d_0_1(m)
  mean([ D*r == zeros(m) for r in rs])
end

function experiment_with_exact_bound(m)
    randomD() = rand(0:9, m, m)
    Ds = Lazy.repeatedly(1_000, randomD)
    maximum([exact_bound(D) for D in Ds])
end

function experiment_with_estimate_bound(m)
    randomD() = rand(0:9, m, m)
    Ds = Lazy.repeatedly(1_000, randomD)
    maximum([bound(D) for D in Ds])
end

#print(d_0_1(3))

