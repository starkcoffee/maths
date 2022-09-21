
function verifyId(f, g, d)
  x = rand(1:100*d)

  n = 3
  for i = 1:n
    are_equal = f(x) == g(x) 

    if !are_equal
      println("not equal")
      return
    end
  end

  if n > d
    println("are equal")
  else
    pr = 1 - 1/(100*d)^n
    println("equal with a probability >= $pr")
  end

end

verifyId(x -> x^2, x -> (x-1)*(x-2), 2)
verifyId(x -> x^2, x -> x^2, 2)
verifyId(x -> x^5 + 11*x^4 - 321*x^3 + 865*x^2 + 3200*x - 7500, x -> (x-5)*(x-10)*(x+3)*(x-2)*(x+25), 5)
