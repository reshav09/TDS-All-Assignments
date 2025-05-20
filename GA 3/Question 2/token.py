import requests
import json

# Variables
url = "https://aipipe.org/openai/v1/responses"
authorization_token = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDU0MzBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.Z3NiJsvjgYnpVX5vTKIb7oVP5Kd2TwOrhp4TJoORcIM"  # Replace with your actual token
input_data = "List only the valid English words from these: L2huvHK, TpAu, 3JLnr, HsdxV, kRLBEgSl, xy, XDYOrl, vKEHWS5z, vmusJiO, kr7iTKY, 4LS, cizfuEs, E8HMMaD02Y, ojyJjUZ2sr, 5yIVDg, TIsG066fDt, wVFOhm, tC, vOAbDyutjT, yPiMh, x0Oti, r7ZPrtk, gGAYC, nBCqV2pr, wSOOdwIenY, Dn, rD, zoWnO4Vjvo, hU, xTh2mBKN2, uYg4V, YprUwx, UBm, uBTWMTGO, uBDl0PGHYo, J9FWVP, R, Wu, X4, YoJyxzkr, edr3ZNG8, GvhUrHcVpI, Ts, nJ9QCLE4, Gn9qT, m, WoPU, yEaSc02E0u, X82, WzY93AJe7, HFV6x, U, U617N, QCmslKBh, lWl, r, d9rW, 4obRiG, dfEIGEzpw, vAx3, uIT83pb, JDLh6LDH, Zy9P, djB74atxj, QAL1jlID, If4q7DBs, LDKuH0, YkYlL7, vOm, muuon5uV, AWuhKVijO, LEGr, X2iX3B1WwC, etnmPFYZnM, sl, O, pL2858J1, vHcI" # Replace with your actual input data

# Headers and payload
headers = {
    "Authorization": authorization_token,
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4.1-nano",
    "input": input_data
}

# POST request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.status_code)
data = response.json()
print("Input Tokens:", data["usage"]["input_tokens"])
