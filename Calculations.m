% Laser
las_pow = 20*1000; %W
las_freq = 33.33; %hz
energy_pulse = 600; %J

G = 6.6743*10^(-11);
M = 5.9722 * 10^24;
R = 6371*1000;

% Kinetic Energy
vel = 10*1000; %m/s
mass = 0.1; % kg
KE = (1/2) * mass * vel^2;
velocity = [];
orbital_vel = sqrt(9.81*(R+500*1000))/1000 %Km
plot_orbit = zeros(100, 1) + orbital_vel;

for i= 1:100
    KE = KE - (energy_pulse*las_freq);
    new_vel = sqrt(2*KE / mass);
    velocity(i) = new_vel/1000;
end 

figure(1)
i = 1:100;
plot(i, velocity, "LineWidth",2)
hold on
plot(i,plot_orbit, "LineWidth", 5)
hold off
title("Velocity vs Number of energy pulses hit")
ylabel("Velocity Km/s")
xlabel("Number of energy pulses hit")
legend("Debri Velocity", "Critical Orbital Velocity")

final_velocity = velocity(end)