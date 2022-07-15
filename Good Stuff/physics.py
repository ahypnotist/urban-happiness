import math

#BELOW THIS DO NOT CHANGE ANYTHING IF YOU ARE JUST TRYING TO RUN A CALCULATION


def full_print(variable, measure):
    full = str(variable) + measure
    print(full)

# important constants

pi = math.pi
twopi = 2 * pi
gravity = 9.8
reverse_gravity = -9.8

#the rule for these functions is that when a variable is left to "solve", the function will solve for it

#sometimes variable names are reused, but it's fine because these functions don't really interact anyway

#2nd law of newton


def newton_fma(newton_force, newton_mass, newton_acceleration):
    if newton_force == "solve":
        #f = ma
        newton_force = newton_mass * newton_acceleration
        full_print(newton_force, "N")
    elif newton_mass == "solve":
        #m = f / a
        newton_mass = newton_force / newton_acceleration
        full_print(newton_mass, "kg")
    else:
        #a = f / m
        newton_acceleration = newton_force / newton_mass
        full_print(newton_acceleration, "m/s²")


#rectilinear motion


def rlm_velocity(velocity, time, distance):
    if velocity == "solve":
        # v = t / d
        velocity = time / distance
        full_print(velocity, "m/s")
    elif time == "solve":
        #t = d / v
        time = distance / velocity
        full_print(time, "s")
    else:
        distance = time * velocity
        full_print(distance, "m")


def rlm_acceleration(initial_velocity, final_velocity, time, acceleration, distance):
    if acceleration == "solve" and distance == "solve":
        acceleration = (final_velocity - initial_velocity) / time
        full_print(acceleration, "m/s²")
        distance = (initial_velocity * time) + (0.5 * (acceleration * (time ** 2)))
        full_print(distance, "m")
    elif acceleration == "solve":
        acceleration = (final_velocity - initial_velocity) / time
        full_print(acceleration, "m/s²")
    elif distance == "solve":
        #V0T + 1/2at^2
        distance = (initial_velocity * time) + (0.5 * (acceleration * (time ** 2)))
        full_print(distance, "m")


#a pendulum

def pendulum(time, length):
    if time == "solve":
        time = twopi * (math.sqrt(length / gravity))
        full_print(time, "s")


def free_fall(direction, height, final_velocity, initial_velocity, time):
    #direction is where its falling, be it down or up
    #if the direction is up, reverse gravity is used
    #hint: if the problem says that the person threw it up, the direciton is up.
    if direction == "down":
        if time == "solve":
            time = (final_velocity - initial_velocity) / gravity
            full_print(time, "s")
        elif 
    else:
        if time == "solve":
            time = (final_velocity - initial_velocity) / reverse_gravity
            full_print(time, "s")


#ABOVE THIS DON'T CHANGE ANYTHING IF YOU ARE JUST RUNNING

#BUT DO READ IT BECAUSE IT HAS SOME HElPFULl NOTES TO USE IT

rlm_acceleration(9, 4, 7, False, False)
