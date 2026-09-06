# 方法1：使用print直接输出类型信息
print(type("罗嘉意"))
print(type(666))
print(type(11.345))

# 方法2：使用变量储存type()语句的结果
String_type = type("罗嘉意")
int_type = type(11)
float_type = type(11.123)
print(String_type)
print(int_type)
print(float_type)

# 方法3： 使用type()语句，查看变量中储存的数据类型信息
name = "海南师范大学"
name_type = type(name)
print(name_type)