% Laser
las_pow = 20*1000; %W
las_freq = 33.33; %hz
energy_pulse = 600; %J

% Kinetic Energy
vel = 10*1000; %m/s
mass = 0.1; % kg
KE = (1/2) * mass * vel^2;
velocity = [];
for i= 1:100
    KE = KE - (energy_pulse*las_freq)
    new_vel = sqrt(2*KE / mass)
    velocity(i) = new_vel;
end 

figure(1)
i = 1:100;
plot(i, velocity)