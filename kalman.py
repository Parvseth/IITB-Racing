import numpy as np
import matplotlib.pyplot as plt
import random


aromas = 0
h1  = 10
h2 = 20
h3 = 30

velocity = random.uniform(0, 1)
current_pos = 0
current_state = np.matrix([[current_pos], [velocity]])  # Position and velocity as a column vector
delT = 0.5
A = np.matrix([[1, delT], [0, 1]])                          # State transition matrix
P = np.matrix([[1, 0], [0, 1]])                             # Initial covariance matrix
R = np.matrix([[1, 0], [0, 1]])                             # Process noise covariance matrix
C = np.matrix([[1,0],[0,1]])                 # doubt 
Q = np.matrix([[1,0], [0,1]])                # measurement noise   ; taken constant for once

mean_array = np.array([])
covariance_array = np.array([])

def prediction(current_state, A, P, R):
        new_velocity = random.uniform(0, 5)  # Random float between 0 and 5

        current_state[1, 0] = new_velocity  # Update the velocity in the state vector
        
        
        next_state = A * current_state             # Predict the next state    which involves previous state + control input*t ; 
        
        
        P = A * P * A.T + R                # Predict the next covariance        and it represents the uncertainity in the state prediction 
        
        return next_state, P


def update(P ,H, Q ,predicted_state , measured_position):
        
        K = P * H.T * np.linalg.inv(H * P * H.T + Q)        # kalman gain
    
        y = np.matrix([[measured_position]])  # Measurement matrix

        updated_state = predicted_state + K * (y - H * predicted_state)
        
        I = np.eye(P.shape[0])  # Identity matrix

        P = (I - K * H) * P
        return updated_state, P
    

x = np.linspace(0,30,40)
x_axis = x.tolist()


for i in range(0,40): 
    
    # next_state = predicted_mean
    # P = predicted covariance

    predicted_mean , predicted_covariance = prediction(current_state ,A,P,R)


    true_position = current_state[0, 0] + current_state[1, 0] * delT
    
    # Generate the measured position with Gaussian noise
    measured_position = true_position + random.gauss(0, np.sqrt(Q[0, 0]))   

    next_state, next_P = update(predicted_covariance, C, Q, predicted_mean,measured_position ) # found mean and covariance
    
    # mean_array.append(next_state)
    # covariance_array.append(next_P)


    
    y_axis = []
    y_axis1 = []
    y_axis2 = []

    for xi in x_axis :
        y=((1/np.sqrt(2*np.pi*next_P[0,0]))*np.exp((-0.5*next_P[0,0])*(xi-next_state[0,0])**2))
        y_axis.append(y)
    for xi in x_axis :
        y1=((1/np.sqrt(2*np.pi*Q[0,0]))*np.exp((-0.5*Q[0,0])*(xi-true_position)**2))
        y_axis1.append(y1)
    for xi in x_axis :
        y2=((1/np.sqrt(2*np.pi*Q[0,0]))*np.exp((-0.5*Q[0,0])*(xi-measured_position)**2))
        y_axis2.append(y2)
    
    
    if (next_state[0,0] >= 9 and next_state[0,0] <=11)  or (next_state[0,0] >= 19 and next_state[0,0] <=21) or (next_state[0,0] >= 29 and next_state[0,0] <=31)  :
        plt.plot(x_axis, y_axis)
        plt.plot(x_axis, y_axis1)
        plt.plot(x_axis, y_axis2)        

        plt.show()
    


    current_state = next_state 
    P = next_P


