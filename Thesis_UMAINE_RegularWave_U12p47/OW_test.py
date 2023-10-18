import math

def generate_wave_file(amplitude, period, timestep, total_time):
    # Calculate the number of time steps
    num_steps = int(total_time / timestep)
    omega = 2*math.pi / period
    # Open the file for writing
    with open("FromFile_IncidentWave", "w") as file:
        # Write header
        file.write("#OceanWave\n")
        file.write(str(timestep) + "\n")
        file.write("0\n")  # Initial condition for zeta

        # Write wave elevations for each time step
        for step in range(num_steps):
            time = step * timestep
            zeta = amplitude * math.cos(omega * time)
            file.write("{:.6f}\n".format(zeta))

# User-defined parameters
A = 5  # Amplitude
period = 13  # Frequency, for instance 2*pi for 1 Hz
timestep = 0.2  # Time step
total_time = 240.0  # Total simulation time

generate_wave_file(A, period, timestep, total_time)

