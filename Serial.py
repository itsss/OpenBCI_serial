import serial
import binascii
sampNumb = ""
channel_data = [0,0,0,0,0,0,0,0,0]
accel_data = [0,0,0]
gain = 24
Vref = 4.5
# scale_fac_uVolts_per_count = Vref/float((pow(2,23)-1))/gain*1000000.
scale_factor = Vref / (gain * ((2 ** 23) - 1))
i = 0
with serial.Serial('COM8', 115200, timeout = 1,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
    ser.write('b')
    while(1):
        s = ser.read(1)
        if binascii.hexlify(s) == "a0":
            sample = ser.read(31)
            sampleID = sample[0]
            channel_data[1] = sample[1:4]   # Data
            channel_data[2] = sample[4:7]
            channel_data[3] = sample[7:10]
            channel_data[4] = sample[10:13]
            channel_data[5] = sample[13:16]
            channel_data[6] = sample[16:19]
            channel_data[7] = sample[19:22]
            channel_data[8] = sample[22:25]

            accel_data[0] = sample[25:27]  # Accel X
            accel_data[1] = sample[27:29]  # Accel Y
            accel_data[2] = sample[29:31]  # Accel Z

            print(str(int(binascii.hexlify(channel_data[1]), 16) * scale_factor) + "\t" + str(
                int(binascii.hexlify(channel_data[2]), 16) * scale_factor) + "\t" + str(
                    int(binascii.hexlify(channel_data[3]), 16) * scale_factor)+ "\t" + str(
                        int(binascii.hexlify(channel_data[4]), 16) * scale_factor)+ "\t" + str(
                            int(binascii.hexlify(channel_data[5]), 16) * scale_factor))
