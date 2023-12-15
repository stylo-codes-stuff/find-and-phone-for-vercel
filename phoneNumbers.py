import phonenumbers


def get_line_type(number):
    number = phonenumbers.parse(number, None)
    switch = {
        0: "Fixed Line",
        2: "Fixed Line or Mobile",
        1: "Mobile",
        8: "Pager",
        7: "Personal Use",
        4: "Premium Rate",
        5: "Shared Cost",
        3: "Toll Free",
        9: "UAN",
        99: "Unknown",
        10: "Voicemail",
        6: "VOIP",
    }
    return switch.get(phonenumbers.number_type(number), "nothing")


def getinformation(number):
    number = number.replace(" ", "-")
    number = "+" + number
    num_data = {"Number": number, "Valid": [], "Region Code": [], "Line Type": []}
    num = phonenumbers.parse(number, None)
    if phonenumbers.is_valid_number(num):
        num_data["Valid"].append("Yes")
        num_data["Region Code"].append(phonenumbers.region_code_for_number(num))
        num_data["Line Type"].append(get_line_type(number))
        return num_data
    else:
        del num_data["Region Code"]
        del num_data["Line Type"]
        num_data["Valid"].append("No")
        return num_data
