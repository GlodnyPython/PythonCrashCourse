bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # -1 zawsze oznacza ostatni item w liscie
print(bicycles[-2]) # -2 i kolejne ocznaczaja odpowiednio 2 i kolejne itemy od konca

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
