from Crypto.Util.number import long_to_bytes

# assuming you have the value of d
d = 0x6f535e1b5e1b061b0c020f0b0b10134f535e1b4852555c575e1b59424f5e1b4f535a4f1b4c5a481b4354495e5f121b0112

# given values
ct = 90411409551177819360717236462351545237822367597930505531741437834918499125195272674859389978951589180632146502190429979348445123366914000167832349866368754227474060832624537550600921894849466284315037863094795265822884392628050584343158613338754532642964368052098136565157343201877382609610774291396944124354
n = 10425866553433272288676977376976736493869099145622614885498170561565122111495807572631609087909399078701783905493563029715011322065331636751277834978526061 * 9215753518399683669080201592666232851634627861957009698720674021492716071355990364002777325458055207969176695525292834842774295594232711456066623178861093

# decrypt the ciphertext
m = pow(ct, d, n)

# convert the number back to bytes
flag = long_to_bytes(m)

print(flag)
