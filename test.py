from signify.authenticode.signed_pe import SignedPEFile


times = []

# https://signify.readthedocs.io/en/latest/authenticode.html
with open("memtest.efi.mui", "rb") as f:
    pefile = SignedPEFile(f)
    for signed_data in pefile.signed_datas:
        print(signed_data.signer_info.program_name)
        if signed_data.signer_info.countersigner is not None:
            print(signed_data.signer_info.countersigner.signing_time)
            times += [signed_data.signer_info.countersigner.signing_time]

assert times == ["2016-08-06T11:59:52.180000+00:00"]
