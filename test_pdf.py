from pathlib import Path

eicar = r'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

pdf = f"""%PDF-1.4
% RebillGuard antivirus pipeline test
1 0 obj
<< /Type /Catalog >>
endobj
% {eicar}
%%EOF
"""

Path("rebillguard-eicar-test.pdf").write_bytes(pdf.encode("ascii"))
print("Created rebillguard-eicar-test.pdf")