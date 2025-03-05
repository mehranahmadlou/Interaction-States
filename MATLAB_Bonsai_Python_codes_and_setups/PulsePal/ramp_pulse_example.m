% PulsePal('COM4')
RampWaveVoltages = 3.3*[0:0.002:1 ones(1,3698) 1:-0.002:0];
ProgramPulsePalParam(1, 14, 1);
SendCustomWaveform(1, 0.001, RampWaveVoltages);
for i = 1:4
    TriggerPulsePal(1); pause(5)
end