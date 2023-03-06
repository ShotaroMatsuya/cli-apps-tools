using ArgParse

function main()
  settings = ArgParseSettings(description="Simple CLI with Julia", version="0.01", add_version=true, epilog="Additional Description")

  @add_arg_table settings begin
    "operation"
    help = "Specify Operation"
    arg_type = String
    "number1"
    help = "Number"
    arg_type = Int
    "number2"
    help = "Number"
    arg_type = Int
  end

  # NameSpace
  args = parse_args(settings)
  println(args)
  
  if args["operation"] == "add"
    println(args["number1"] + args["number2"])
  elseif args["operation"] == "subtract"
    println(args["number1"] - args["number2"])
  end
end


main()