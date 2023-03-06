using Fire

"Register User"
@main function register(firstname::AbstractString)
  print("Hello $firstname")
end

"Greet A User"
@main function greet(firstname::AbstractString)
  println("Good morning ", firstname[end:-1:1])
end

"Add Salary"
@main function add_salary(num::Integer...)
  println("Adding numbers::", num)
  println(sum(num))
end