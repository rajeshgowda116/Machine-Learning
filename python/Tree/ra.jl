println("Enter frist complex number(real part)")
r1=parse(Float64,readline())
println("Enter the frist complex num(imaginary part)")
i1=parse(Float64,readline())
println("Enter the second complex num(real part)")
r2=parse(Float64,readline())
println("Enter the second complex num(imaginary part)")
i2=parse(Float64,readline())
c1=complex(r1,i1)
c2=complex(r2,i2)
println("Addition:",c1+c2)
println("Subtraction:",c1-c2)
println("")



