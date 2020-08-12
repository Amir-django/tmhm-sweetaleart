class facilitator_login(View):
    
    def get(self, request):
        return render(request,'facilitators/index.html')


    #authentication_classes = (TokenAuthentication,) 
    #permission_classes = (IsAuthenticated,) 
    def post(self, request):
        if request.method == 'POST':
            email1 =  request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email1, password=password)
            message=None

            try:
                obj = Token.objects.get_or_create(user=user)
                appli = Applicants.objects.get(user=user)   #appli.Aid
                approved = Facilitator.objects.get(user=appli) #aprroved.Fid
                print(obj)
            except:
                obj = None
                approved=None

            if approved:
                if obj:
                    if user:
                        if user.is_active:
                            login(request, user)
                            context = {'approved':approved}
                            return render(request, 'facilitators/Dashboard/index.html', context)
                            return response(obj, status=200)
                        else:
                            return HttpResponse("Account not active")
                    else:
                        print("someone tried to login and failed")
                        return HttpResponse("You are not a facilitator")
                else:
                    return HttpResponse("you are not authorized")
            else:
                msg = "not a facilitaotr"
                return render(request, 'facilitators/index.html',{'msg':msg})
