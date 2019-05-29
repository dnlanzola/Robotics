function [A0_all_trackable, pos_all_trackable, nframe, ntrackable, trackableID] ...
    = read_patriot_data_hemis_twosensor(filename)
% derived from read_patriot_data_hemis()
% read patriot data file with up to two sensors.
% the file may have one OR two sensor data. This code should be able to 
% process both.
%
% 07/11/2016

M = csvread(filename);

% determine number of trackables (actually, number of sensors)
ncol = size(M, 2);
if ncol == 15
    ntrackable = 2;
elseif ncol == 8
    ntrackable = 1;
else
    error('number of columns of patriot data file is neither 8 nor 15.');
end

% get trackable ID
trackableID = zeros(1, ntrackable);
for i = 0:ntrackable-1
    trackableID(i+1) = M(2, 2 + i*7);
end

nframe = size(M, 1) - 1;

A0_all_trackable  = cell(1, ntrackable); % includes all 6dof data
pos_all_trackable = cell(1, ntrackable); % all position of trackable

angular_velocity = [];
skewM = zeros(3,3);



for i = 0:ntrackable-1

    %% TA's notes: get position and orientation from the patriot.csv file. No need to modify.
    pos = M(2:end, (3 + i*7):(5 + i*7))' / 100; % convert from centimeter to meter
    ori = M(2:end, (6 + i*7):(8 + i*7))' * pi / 180; % convert from degree to radians
    
    
    
    
    A0_all_trackable{i+1} = cell(1, nframe);
    pos_all_trackable{i+1} = zeros(3, nframe);
    
    %FIRST R SAVED
    R_first = euler2rotm(ori(:, 1));
    Rd_first = euler2rotm_derivate(ori(:, 1));
    d_first = pos(:, 1);  %First point in graph
    
    
    for f = 1:nframe
        %% TA's Notes: the function 'euler2rotm' takes the orientation data from the patriot.csv file
        %%      and converts it into the rotation matrix based on Eq. 2.65 in the textbook.
        
        %% Flip plane for loose nut
        %ori(3, f) = ori(3, f) + pi;
        
        
        
        
        R = euler2rotm(ori(:, f)); % rotation matrix in patriot frame
        
        
       Rd = euler2rotm_derivate(ori(:,f)); % derivate of rotation matrix in patriot frame 
        

        
        %MULTIPLY FIRST ROTATION MATRIX BY EVERY OTHER ONE.
        R = R * R_first;
        
        Rd = Rd * Rd_first;

        
        skewM = R.' * Rd; 
         
        
        
        %% TA's Notes: the position data (x,y,z) is taken from the file and put into a vector form here:
        d = pos(:, f);

        d = d - d_first;
        
        %% TA's Notes: the rotation R and the position d are taken together to form a homogeneous transformation matrix 
        %%  (based on Eq. 2.91 in the textbook)
        A2 = [R            d;
              zeros(1, 3)   1];

        %% TA's Notes: you'll have to do some coordinate system transformation here to get it with respect of the tool.


        
        
        %% Question 6 a) done here. You should also calculate the linear and angular velocities here since you
        %%  will have access to the (x,y,z) and orientation.
        %% -- perform your functions here before inputting it into patriot_frame2_to_0_transfm(...) function.

        
        
        
        
        %% TA's Notes: the Patriot's frame is different to that of the viewer. This part 
        %%      changes its coordinate system to that of the interface.
        %% -- remember that A0 and A2 are homogeneous transformation matrices. You will need to compute inverse of it 
        %%      in a different way than usual.
        A0 = patriot_frame2_to_0_transfm(A2);

        %% TA's notes: use the angular velocity equation to obtain the skew matrix and then take the values for x, y, z:
        %%      You can probably save everything into a matrix and use it to generate plots.
        %% ang = ......; 
        %% angular_velocity = [angular_velocity; ang];
        
        A0_all_trackable{i+1}{f} = A0;
        pos_all_trackable{i+1}(:, f) = A0(1:3, 4);

    end
end


%% TA's Notes: the position and orientation stays within the scope of this file. You should perform your operations here
%%      while you have easier access to it; otherwise, you will need to access the data stored within cell structures 'A0_all_trackable'.
linear_velocity = [];


linear_velocity(1,1) = "x";
linear_velocity(1,2) = "y";
linear_velocity(1,3) = "z";
linear_velocity(1,5) = "f";


for i = 3 : nframe
    %% calculate the velocity from one point to another using the positions (they are stored in pos)
    %%  -- linear_velocity = [linear_velocity; temp;];
    
     linear_velocity(i-1, 1) = (M(i, 3) - M(i - 1, 3)) / (M(i, 1) - M(i-1, 1));
    
     linear_velocity(i-1, 2) = (M(i, 4) - M(i - 1, 4)) / (M(i, 1) - M(i-1, 1));
     
     linear_velocity(i-1, 3) = (M(i, 5) - M(i - 1, 5)) / (M(i, 1) - M(i-1, 1));
     
     linear_velocity(i-1, 5) = i - 2;
     
    Test = 1;
end
x = linear_velocity(:, 5);
y = linear_velocity(:, 1);
plot(x,y);

csvwrite("linear_velocity.csv", linear_velocity);

%% TA's Notes: Try using 3D plots such as scatter3, comet3, etc. for those which require 3D visualization.
%%      Otherwise, use regular subplot/plot for anything that can be visualized in 1D/2D.
