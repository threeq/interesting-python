import pithy_table

pithy_table.pithy_table()

print("===================\n")
pithy_table.pithy_table_align()


print("===================\n")
pithy_table.pithy_table_align_n(3)

print("===================\n")
pithy_table.pithy_table_align_n(1)


print("===================\n")
pithy_table.pithy_table_align_n(20)


print("===================\n")
pithy_table.pithy_table_align_n_file(10)

print(" to file ===================\n")
f = open('out/table-10.txt', "w+")
pithy_table.pithy_table_align_n_file(10, f=f)
f.close()

with open("out/table-6.txt", "w+") as f:
    pithy_table.pithy_table_align_n_file(6, f=f)


print(" to max file ===================\n")
with open("out/table-4000.txt", "w+") as f:
    import datetime as d
    s = d.datetime.now()
    pithy_table.pithy_table_align_n_file(10000, f=f)
    e = d.datetime.now()
    print("duration 耗时：%s" % (e-s))

print(" to max file ===================\n")
with open("out/table-4000-max.txt", "wb") as f:
    import datetime as d
    s = d.datetime.now()
    pithy_table.pithy_table_align_n_file_max(10000, f=f)
    e = d.datetime.now()
    print("duration 耗时：%s" % (e-s))
