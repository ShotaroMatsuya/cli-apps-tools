using ArgParse

function main()
  settings = ArgParseSettings(description="Simple CLI with Julia", version="0.01", add_version=true, epilog="Additional Description")

  @add_arg_table settings begin
    "--firstname", "-f"
    help = "Specify First name"
    arg_type = String
  end

  # NameSpace
  args = parse_args(settings)
  println(args)
  println(args["firstname"])
end


main()