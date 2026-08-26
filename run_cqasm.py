"""
STEP 1:

To install QX, run the following command on Anaconda/Linux Terminal 
>> pip install --default-timeout=100 qxelarator==0.5.3 
"""

"""
STEP 2:

Make a Python program run_cqasm.py with the following content:
"""
import sys
import qxelarator
qc_fname = sys.argv[1]      # Get the QASM filename from the command line
qx = qxelarator.QX()        # Define a QX object
qx.set(qc_fname)            # Set the filename to the QX object
qx_output = qx.execute()    # Execute the QASM file and get the output
print(qx_output)            # Print the output from QX simulator

# Note: Do NOT use this command. You will get AttributeError: module 'qxelarator' has no attribute 'execute_file'
# print(qxelarator.execute_file(sys.argv[1]))

"""
STEP 3:

Write your quantum code in the <filename>.qc and place it in the same directory as the run_cqasm.py file
"""

"""
STEP 4:

To execute and simulate the file, run the following command on Anaconda/Linux Terminal 
>> python run_cqasm.py <filename>.qc
"""