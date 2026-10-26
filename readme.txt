========================================================================
                 STEGOSHIELD - USER GUIDE
========================================================================
StegoShield lets you:
1)Hide secret text inside PNG images (steganography)
2)Decode hidden text, analyze pixel changes
3)View activity logs

------------------------------------------------------------------------
1. SETUP & RUN
------------------------------------------------------------------------
1. Install requirements:
   pip install -r requirements.txt

2. Run the program:
   python main.py


------------------------------------------------------------------------
2. HOW TO USE THE TABS
------------------------------------------------------------------------

[ ENCODE ]
- Select a source PNG image using "Browse".
- Select where to save your output image using "Browse".
- Type your secret message.
- Click "Encode".

[ DECODE ]
- Select an image with a hidden message using "Browse".
- Click "Decode Message" to read the hidden text.

[ FORENSIC ANALYSIS ]
- Select an image using "Browse".
- Click "Analyze Image" to view pixel bit distribution graphs.

[ AUDIT LOGS ]
- Open this tab to see a live list of all actions performed.
- Logs are also saved automatically to `audit_log.txt`.

========================================================================