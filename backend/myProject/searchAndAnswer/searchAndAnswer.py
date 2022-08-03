
def searchAndAnswer(strFiles, firstName, lastName, idNumber):
    res = []
    status = '1'
    yearToday = ["תשפ''ב", 'תשפב']

    if not any(element == 'אישור' for element in strFiles[1]) or not any(element in 'לימודים' for element in strFiles[1]):
        res.append('The uploaded study certificate file is not a study certificate')
        status = '0'

    if not any(element in idNumber for element in strFiles[0]):
        res.append('The ID number in the ID card is incorrect')
        status = '0'
    if not any(element == idNumber for element in strFiles[1]):
        res.append('The ID number in study certificate is incorrect')
        status = '0'
    if not any(element == idNumber for element in strFiles[2]):
        res.append('The ID number in the student card is incorrect')
        status = '0'
    if not any(element == firstName for element in strFiles[0]) or not any(element == lastName for element in strFiles[0]):
        res.append('The name in the ID card is incorrect')
        status = '0'
    if not any(element == firstName for element in strFiles[1]) or not any(element == lastName for element in strFiles[1]):
        res.append('The name in the certificate is incorrect')
        status = '0'
    if not any(element == firstName for element in strFiles[2]) or not any(element == lastName for element in strFiles[2]):
        res.append('The name in student card is incorrect')
        status = '0'
    if not any(element == firstName for element in strFiles[3]) or not any(element == lastName for element in strFiles[3]):
        res.append('The name in rav-kav is incorrect')
        status = '0'
    if not any(element == yearToday[0] for element in strFiles[1]) and not any(element == yearToday[1] for element in strFiles[1]):
        res.append('The date in the certificate is incorrect')
        status = '0'
    return [status, res]



