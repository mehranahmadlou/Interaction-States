# Connect breakout board 1.2 to the computer, plug in the 12V power supply.  
# Connect a Poke to port 3 of the breakout board. When you break the IR beam of 
# the Poke the LED and solenoid will turn on.

from pyControl.utility import *
from devices import *
from devices import Breakout_1_2, Poke, Audio_board, Lickometer

# Define hardware

board = Breakout_1_2()
poke  = Poke(board.port_2, rising_event='poke', falling_event='poke_out', debounce=5)
lickometer  = Lickometer(board.port_1, rising_event_A='lick_detect', falling_event_A='lick_off',rising_event_B='lick_2', falling_event_B='lick_2_off', debounce=50)                     
speaker = Audio_board(board.port_3)
optogenetic = Digital_output(pin=board.BNC_1, inverted=False, pulse_enabled=True)
movie_start = Digital_input(pin=board.BNC_2, rising_event='movie_onset')

# State machine

states = ['wait_for_poke','poked_reward_available','reward']

events = ['poke', 'poke_out','lick_detect','lick_off','sound_off','session_timer','OptoReady','OptoOff','movie_onset']

initial_state = 'wait_for_poke'


# Variables

v.state_dur = 500
v.volume = 0
speaker.set_volume(v.volume+50)
v.ratio = 1
v.session_duration = 60 * minute
v.reward_duration = 250 * ms
v.rewards_obtained = 0
v.opto = 0
v.disengaged = 90 * second
v.poke = 2
v.disengage = 0


# Run start and stop behaviour. 40

def run_start(): 
    # Set session timer and turn on houslight.
    set_timer('session_timer', v.session_duration)                              

def run_end():
    # Turn off all hardware outputs.  
    stop_framework()

# poke and reward state/behaviour 50

def wait_for_poke(event):
    set_timer('OptoReady', v.disengaged)
    poke.LED.on()
    if event == 'poke':
	v.opto = 0
	v.poke += 1
	if v.poke == 1:
            v.disengage = 0
            optogenetic.pulse(20, duty_cycle=50, n_pulses=False)
            v.opto = 1
            set_timer('OptoOff', 180 * second)
        goto_state('poked_reward_available')

def poked_reward_available(event):
    disarm_timer('OptoReady')
#    if v.opto == 1
#    set_timer('OptoOff', v.disengaged)
    if event=='entry':
        poke.LED.off()
#        poke.SOL.on()
#	poke_photometry.on()
    elif event=='exit':
        poke.LED.off()
#        poke.SOL.off()
#	poke_photometry.off()
    elif event == 'poke_out':
	speaker.noise()
#	speaker.click()
#	speaker.sine(4000)
	set_timer('sound_off', 1*second)
	v.opto = 0
    elif event == 'lick_detect':
#	optogenetic.off()
	v.opto = 0
#	print('Opto Off: {}'.format(v.opto))
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
	optogenetic.off()
	movie_start.off()
        stop_framework()
        disarm_timer('OptoReady')
    if event == 'sound_off':
	speaker.off()
    if event == 'OptoReady':
	v.poke = 0
	print('Opto On: {}'.format(v.opto))
    if event == 'OptoOff':
        disarm_timer('OptoReady')
        v.poke = 2
        optogenetic.off()
	print('Opto Off')
	stop_framework()
