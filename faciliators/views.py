@api_view(['GET', 'POST'])
def facilitator_Profile_page(request, pk):

    if request.method == 'GET':
        ourdata = Facilitator.objects.get(Fid=pk)   
        ourname = ourdata.name.split()
        firstname = ourname[0]
        lastname = ourname[1]

        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,'pk':pk}
        return render(request, 'facilitators/Dashboard/profile.html',context)

    if request.method == 'POST':
        ourdata=Facilitator.objects.get(Fid=pk)
        #profileimg = request.FILES
        #for i in request.FILES:
        if request.FILES:
            ourdata.profile=request.FILES['profile']

        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        ourdata.name=firstname+" "+lastname
        ourdata.phone = request.POST['phone']
        #ourdata.Bio = request.POST['Bio']
        ourdata.country = request.POST['country']
        ourdata.state = request.POST['state']
        ourdata.PAddress = request.POST['addressLine1']
        ourdata.TAddress = request.POST['addressLine2']
        ourdata.zipcode = request.POST['zipCode']
        
        ourdata.save()
        msg = "profile saved"
        context = {'ourdata':ourdata, 'firstname':firstname, 'lastname':lastname,'msg':msg}
        return render(request, 'facilitators/Dashboard/profile.html', context)

    #context = {'ourdata':ourdata}
    return render(request, 'facilitators/Dashboard/profile.html', context)
