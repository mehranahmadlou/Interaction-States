# Connect breakout board 1.2 to the computer, plug in the 12V power supply.  
# Connect a Poke to port 3 of the breakout board. When you break the IR beam of 
# the Poke the LED and solenoid will turn on.

from pyControl.utility import *
from devices import Breakout_1_2, Poke, Audio_board,Lickometer

# Define hardware

board = Breakout_1_2()
poke  = Poke(board.port_2, rising_event='poke', falling_event='poke_out', debounce=5)
lickometer  = Lickometer(board.port_1, rising_event_A='lick_detect', falling_event_A='lick_off',rising_event_B='lick_2', falling_event_B='lick_2_off', debounce=50)                     
speaker = Audio_board(board.port_3)

# State machine

states = ['wait_for_poke','poked_reward_available','reward']

events = ['poke', 'poke_out','lick_detect','lick_off','sound_off','session_timer']

initial_state = 'wait_for_poke'


# Variables

v.state_dur = 500
v.volume = 0
speaker.set_volume(v.volume+50)
v.ratio = 1
v.session_duration = 30 * minute
v.reward_duration = 700 * ms  
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
    poke.LED.on()
    if event == 'poke':
        goto_state('poked_reward_available')

def poked_reward_available(event):
    if event=='entry':
        poke.LED.off()
#        poke.SOL.on()
    elif event=='exit':
        poke.LED.on()
#        poke.SOL.off()
    elif event == 'poke_out':
	speaker.noise()
#	speaker.click()
#	speaker.sine(4000)
	set_timer('sound_off', 1*second)
	    #set_timer('sound_off', 1*second)
	    #if event == 'sound_off':
	        #speaker.off()
    elif event == 'lick_detect':
        goto_state('reward')

def reward(event):
    # On entry turn on solenoid and set timer, when timer elapses goto_state
    # 'wait_for_poke' state, on exit turn of solenoid. 
    if event == 'entry':
        timed_goto_state('wait_for_poke', v.reward_duration)
	lickometer.SOL_1.on()
        v.rewards_obtained += 1
        print('Rewards obtained: {}'.format(v.rewards_obtained))
    elif event == 'exit':
	#pause_timer('lick_detect', 1*second)
	#unpause_timer('lick_detect')
	#set_timer('lick_off', 3*second)
        lickometer.SOL_1.off()
#    elif event == 'lick_off':
#	#set_timer('lick_off', 3*second)
#	#unpause_timer('lick_detect')
#        lickometer.SOL_1.off()
#	timed_goto_state('wait_for_poke', v.reward_duration)


def all_states(event):
    # When 'session_timer' event occurs stop framework to end session.
    if event == 'session_timer':
        stop_framework()
    if event == 'sound_off':
	speaker.off()