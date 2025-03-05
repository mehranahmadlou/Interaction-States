# Connect breakout board 1.2 to the computer, plug in the 12V power supply.  
# Connect a Poke to port 3 of the breakout board. When you break the IR beam of 
# the Poke the LED and solenoid will turn on.

from pyControl.utility import *
from devices import *
from devices import Breakout_1_2, Poke, Audio_board, Lickometer

# Define hardware

board = Breakout_1_2()
poke  = Poke(board.port_2, rising_event='poke', falling_event='poke_out', debounce=20)
lickometer  = Lickometer(board.port_1, rising_event_A='lick_detect', falling_event_A='lick_off', rising_event_B='lick_2', falling_event_B='lick_2_off', debounce=20)  
#speaker = Audio_board(board.port_3)
trial_start = Digital_output(pin=board.BNC_1, inverted=False, pulse_enabled=True)
#movie_start = Digital_input(pin=board.BNC_2, rising_event='movie_onset')

# State machine

states = ['wait_for_poke','reward','noreward','no_poke']

events = ['poke','poke_out','lick_detect','lick_off','session_timer']

initial_state = 'wait_for_poke'


# Variables

v.state_dur = 100
v.delay = [0.6,0.6,0.7,0.3,0.7,0.4,0.8,0.2,0.7,0.5,0.2,0.7,0.5,0.7,0.5,0.8,0.8,0.6,0.5,0.3,0.5,0.5,0.5,0.2,0.6,0.3,0.3,0.4,0.7,0.8,0.7,0.3,0.5,0.4,0.3,0.6,0.5,0.7,0.5,0.2,0.2,0.7,0.7,0.4,0.4,0.7,0.7,0.5,0.3,0.4,0.6,0.3,0.6,0.3,0.5,0.5,0.4,0.3,0.3,0.4,0.3,0.8,0.8,0.2,0.6,0.8,0.4,0.2,0.3,0.4,0.6,0.8,0.7,0.7,0.4,0.2,0.5,0.2,0.5,0.2,0.7,0.4,0.5,0.4,0.2,0.2,0.6,0.4,0.4,0.2,0.4,0.7,0.6,0.5,0.2,0.3,0.7,0.5,0.6,0.8,0.3,0.6,0.8,0.4,0.3,0.7,0.5,0.2,0.7,0.6,0.6,0.7,0.7,0.5,0.6,0.6,0.2,0.2,0.8,0.6,0.5,0.8,0.6,0.7,0.8,0.8,0.2,0.6,0.3,0.8,0.3,0.2,0.8,0.3,0.6,0.2,0.8,0.6,0.8,0.8,0.4,0.5,0.2,0.4,0.7,0.8,0.3,0.2,0.5,0.6,0.2,0.4,0.7,0.4,0.8,0.3,0.3,0.4,0.8,0.6,0.5,0.7,0.6,0.2,0.5,0.3,0.7,0.5,0.3,0.6,0.4,0.7,0.6,0.4,0.5,0.5,0.7,0.5,0.8,0.6,0.4,0.4,0.8,0.7,0.8,0.3,0.4,0.4,0.2,0.8,0.3,0.7,0.4,0.3,0.7,0.7,0.5,0.7,0.5,0.2,0.8,0.7,0.6,0.4,0.8,0.6,0.3,0.7,0.8,0.4,0.2,0.8,0.6,0.4,0.2,0.3,0.8,0.3,0.2,0.6,0.7,0.8,0.2,0.3,0.5,0.6,0.4,0.6,0.4,0.4,0.2,0.3,0.2,0.6,0.8,0.2,0.3,0.3,0.6,0.5,0.8,0.6,0.4,0.7,0.5,0.4,0.4,0.7,0.3,0.8,0.7,0.6,0.2,0.2,0.8,0.2,0.3,0.8,0.3,0.6,0.5,0.5,0.6,0.4,0.5,0.2,0.6,0.4,0.3,0.8,0.4,0.2,0.8,0.4,0.3,0.8,0.8,0.8,0.8,0.7,0.4,0.7,0.2,0.5,0.3,0.4,0.8,0.6,0.6,0.5,0.8,0.7,0.4,0.8,0.3,0.7,0.6,0.4,0.7,0.5,0.8,0.5,0.3,0.2,0.7,0.7,0.3,0.6,0.7,0.6,0.2,0.7,0.3,0.3,0.7,0.8,0.4,0.6,0.4,0.2,0.5,0.7,0.3,0.5,0.5,0.4,0.5,0.7,0.4,0.7,0.2,0.6,0.5,0.2,0.8,0.4,0.5,0.3,0.2,0.8,0.5,0.8,0.6,0.4,0.7,0.4,0.3,0.8,0.8,0.5,0.6,0.5,0.7,0.6,0.5,0.6,0.3,0.2,0.5,0.5,0.6,0.8,0.5,0.4,0.8,0.7,0.4,0.4,0.3,0.7,0.6,0.3,0.4,0.3,0.2,0.5,0.2,0.2,0.5,0.5,0.7,0.2,0.3,0.6,0.5,0.4,0.3,0.3,0.6,0.5,0.3,0.7,0.6,0.6,0.4,0.3,0.2,0.7,0.2,0.8,0.2,0.5,0.5,0.4,0.6,0.5,0.2,0.5,0.3,0.6,0.3,0.7,0.2,0.7,0.8,0.2,0.6,0.4,0.8,0.4,0.2,0.3,0.6,0.4,0.3,0.2,0.8,0.7,0.6,0.8,0.7,0.5,0.3,0.8,0.7,0.4,0.6,0.8,0.7,0.3,0.6,0.8,0.5,0.8,0.2,0.2,0.3,0.7,0.2,0.4,0.2,0.4,0.8,0.4,0.6,0.3,0.8,0.2,0.7,0.7,0.8,0.8,0.5,0.7,0.2,0.2,0.6,0.6,0.2,0.8,0.5,0.6,0.5,0.2,0.5,0.2,0.4,0.5,0.3,0.4,0.2,0.3,0.4,0.3,0.8,0.5,0.4,0.2,0.3,0.3,0.3,0.4,0.6,0.3,0.6,0.7,0.2,0.2,0.7,0.8]
v.visualstim = [200,0,0,200,0,0,0,200,0,0,0,0,0,0,0,0,0,0,200,200,200,0,200,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,200,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,200,0,0,200,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,200,0,0,0,200,0,0,0,0,0,0,0,0,0,200,0,0,200,200,0,0,0,200,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,200,200,200,0,200,200,0,0,0,200,200,0,0,200,0,200,0,200,0,200,0,0,0,200,0,0,0,0,200,0,0,200,0,200,0,0,200,0,0,0,0,0,0,0,200,0,0,0,0,200,0,0,200,0,200,0,200,0,200,0,0,0,0,0,200,0,0,0,0,200,0,0,0,0,200,0,0,200,0,200,0,200,0,200,0,0,0,0,0,0,0,0,0,0,0,200,0,200,0,0,0,0,0,200,0,0,0,200,200,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,200,0,0,0,0,200,0,0,200,0,0,200,0,0,0,0,0,0,200,0,0,0,0,0,200,0,0,0,0,0,200,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,200,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,200,200,0,0,0,0,200,0,200,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,200,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,200,0,0,200,0,0,200,0,0,200,0,0,0,200,200,0,0,0,0,0,200,0,200,0,0,200,0,0,0,0,0,0,0,0,0,0,200,0,0,0,200,0,0,0,0,200,0,200,200,200,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,200,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,200,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,200,0,0,200,200,0]
v.visual = -1;
v.ratio = 1
v.session_duration = 1440 * minute
v.reward_duration = 75 * ms
v.rewards_obtained = 0

# Run start and stop behaviour.

def run_start(): 
    # Set session timer and turn on houslight.
    set_timer('session_timer', v.session_duration)                              

def run_end():
    # Turn off all hardware outputs.  
    stop_framework()

# poke and reward state/behaviour

def wait_for_poke(event):
    poke.LED.off()
    if event == 'poke':
        trial_start.pulse(100, duty_cycle=50, n_pulses=1)
        v.visual += 1
        y = v.visual
        xx = v.delay[y] + 1.0
        print('Trial')
        if v.visualstim[y] == 0:
            timed_goto_state('reward', xx * second)
            print('Reward: {}'.format(y))
        elif v.visualstim[y] == 200:
            timed_goto_state('noreward', xx * second)
            print('No Reward: {}'.format(y))
#        trial_start.off()
        #lickometer.SOL_1.on()
#    elif event=='poke_out':
        
        
#    elif event == 'lick_detect':
#        goto_state('reward')
#        goto_state('poked_reward_available')

def noreward(event):
    if event=='entry':
        poke.LED.off()
        lickometer.SOL_1.off()
        timed_goto_state('wait_for_poke', 2*second)
    elif event=='exit':
        poke.LED.off()
        lickometer.SOL_1.off()

def reward(event):
    # On entry turn on solenoid and set timer, when timer elapses goto_state
    # 'wait_for_poke' state, on exit turn of solenoid. 
    if event == 'entry':
        timed_goto_state('no_poke', v.reward_duration)
	lickometer.SOL_1.on()
        v.rewards_obtained += 1
        x = v.delay[v.rewards_obtained-1]
        print('Rewards obtained: {}'.format(v.rewards_obtained))
        print('Delay: {}'.format(x))
    elif event == 'exit':
	#pause_timer('lick_detect', 1*second)
	#unpause_timer('lick_detect')
	#set_timer('lick_off', 3*second)
        lickometer.SOL_1.off()

def no_poke(event):
    if event=='entry':
        poke.LED.off()
        lickometer.SOL_1.off()
        timed_goto_state('wait_for_poke', 2*second)
    elif event=='exit':
        poke.LED.off()
        lickometer.SOL_1.off()


def all_states(event):
    # When 'session_timer' event occurs stop framework to end session.
    if event == 'session_timer':
	trial_start.off()
#	movie_start.off()
        stop_framework()
#    if event == 'sound_off':
#	speaker.off()
