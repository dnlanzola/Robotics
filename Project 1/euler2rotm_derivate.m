function R = euler2rotm_derivate(euler)
% assume euler = [phi, theta, psi]
% see function rotm2euler()

phi   = euler(1);
theta = euler(2);
psi   = euler(3);

r11 = (-cos(phi)) * sin(theta) - cos(theta) * sin(phi);
r12 = cos(theta) * cos(phi) * sin(psi) + (-cos(phi) * cos(psi) - sin(theta) * sin(phi) * sin(psi)) + (cos(phi) * cos(psi) * sin(theta) + sin(phi) * sin(psi));
r13 = cos(theta) * cos(phi) * cos(psi) + (-cos(psi) * sin(theta) * sin(phi) + cos(theta) * sin(psi)) + (cos(psi) * sin(phi) - cos(phi) * sin(theta) * sin(psi));

r21 = -sin(theta) * sin(phi) + cos(theta) * cos(phi);
r22 = cos(theta) * sin(phi) * sin(psi) + (-cos(psi) * sin(phi) + cos(phi) * sin(theta) * sin(psi)) + (cos(psi) * sin(theta) * sin(phi) - cos(phi) * sin(psi));
r23 = cos(theta) * cos(psi) * sin(phi) + (cos(phi) * cos(psi) * sin(theta) + sin(phi) * sin(psi)) + (-cos(phi) * cos(psi) - sin(theta) * sin(phi) * sin(psi));


r31 = -cos(theta);
r32 = -sin(theta) * sin(psi) + cos(theta) * cos(psi);
r33 = -cos(psi) * sin(theta) - cos(theta) * sin(psi);

R = [r11, r12, r13;
     r21, r22, r23;
     r31, r32, r33];

end
