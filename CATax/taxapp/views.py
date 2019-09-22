from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from taxapp.models import Tax,TaxDetail
from taxapp.serializers import TaxSerializer,TaxDetailSerializer
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime, timedelta
import iso8601



class TaxViewSet(viewsets.ModelViewSet):
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()

class TaxDetailViewset(viewsets.ModelViewSet):
    serializer_class = TaxDetailSerializer
    queryset = TaxDetail.objects.all()

    def update(self,request,pk=None):
        if TaxDetail.objects.filter(Q(pk=pk) & Q(effectivefromdate=request.data['effectivefromdate']) &
                                    Q(effectivetodate=request.data['effectivetodate'])).exists() is False:
            queryset = TaxDetail.objects.filter(Q(tax__id=TaxDetail.objects.filter(Q(pk=pk)).first().tax.id)).order_by('effectivefromdate')
            # if request.data['effectivetodate'] is not None:
            update_dict={}
            if queryset.filter(Q(effectivefromdate__gte=request.data['effectivefromdate']) &
                                   Q(effectivetodate__lte=request.data['effectivetodate']) if request.data['effectivetodate'] is not None else
                                   Q(effectivetodate__isnull=True)).count() <= 2:


                get_from_qset=queryset.filter(Q(effectivefromdate__lte=request.data['effectivefromdate']) &
                                                  (Q(effectivetodate__gte=request.data['effectivefromdate']) |
                                                   Q(effectivetodate__isnull=True))).first()
                if get_from_qset:
                    from_date=iso8601.parse_date(request.data['effectivefromdate']).date()
                    to_date=iso8601.parse_date(request.data['effectivetodate']).date() if request.data['effectivetodate'] is not None else None
                    #from date lies
                    if get_from_qset.effectivefromdate.date()==iso8601.parse_date(request.data['effectivefromdate']).date():
                        print("create new from {} to {} with id {}".format(get_from_qset.effectivefromdate,to_date,'new id'))
                        print("update id : {} fromdate with {} + 1 day".format(get_from_qset.id,to_date))
                        update_dict['id']=get_from_qset.id
                        update_dict['fromdate_subtract_by_1']=to_date
                    else:
                        print("update id : {} todate with {} - 1 day".format(get_from_qset.id,from_date))
                        update_dict['id'] = get_from_qset.id
                        update_dict['fromdate_add_by_1'] = from_date
                else:
                    print("new from date")

                if request.data['effectivetodate'] is not None:
                    to_date = iso8601.parse_date(request.data['effectivetodate']).date()
                    get_to_qset = queryset.filter(Q(effectivefromdate__lte=request.data['effectivetodate']) &
                                                        (Q(effectivetodate__gte=request.data['effectivetodate']) |
                                                         Q(effectivetodate__isnull=True))).first()
                    if get_to_qset:
                        print("update id : {} fromdate with {} + 1 day".format(get_to_qset.id,to_date))
                    else:
                        print("new todate")
                else:
                    get_larger_row=queryset.filter(Q(effectivefromdate__gt=request.data['effectivefromdate'])).first()
                    if get_larger_row:
                        print('to date is null')
                        print(get_larger_row.id)
                        request.data['effectivetodate']=get_larger_row.effectivefromdate-timedelta(days=1)
                        print(get_larger_row.effectivefromdate-timedelta(days=1))



            else:
                return Response('modifying more than two rows.')





        else:
            return Response("dates are equal.")
            # check country/tax type if changed create new tax with provided detail
            # otherwise update REIT/TaxRate

        # queryset=TaxDetail.objects.filter(Q(tax__id=pk))
        # if queryset.filter(Q(effectivefromdate=request.data['effectivefromdate']) &
        #                             Q(effectivetodate=request.data['effectivetodate'])).exists() is False:
        #     if queryset.filter(Q(effectivefromdate=request.data['effectivefromdate']) &
        #                             Q(effectivetodate=request.data['effectivetodate'])).count()<=2:
        #
        #         #from date conditions
        #         if queryset.filter(Q(effectivefromdate__lte=request.data['effectivefromdate']) &
        #                                 Q(effectivetodate__gt=request.data['effectivefromdate'])).exists() is True:
        #             queryset_from=queryset.filter(Q(effectivefromdate__lte=request.data['effectivefromdate']) &
        #                             Q(effectivetodate__gte=request.data['effectivefromdate'])).first()
        #             print(queryset_from.id)
        #             # if request.data['effectivetodate'] is None and queryset.filter(
        #             #         Q(effectivefromdate__gt=request.data['effectivefromdate'])).count()>1:
        #             #     request.data['effectivetodate']=queryset.filter(
        #             #         Q(effectivefromdate__gt=request.data['effectivefromdate'])).first()
        #         else:
        #             print("new_from_date")
        #
        #         if request.data['effectivetodate'] is not None:
        #             if queryset.filter(Q(effectivefromdate__lte=request.data['effectivetodate']) &
        #                                Q(effectivetodate__gte=request.data['effectivetodate'])).exists() is True:
        #                 queryset_to=queryset.filter(Q(effectivefromdate__lte=request.data['effectivetodate']) &
        #                                 Q(effectivetodate__gte=request.data['effectivetodate'])).first()
        #                 print(queryset_to.id)
        #         else:
        #             print("None")
        # else:
        #     return Response("dates are equal.")
        #     #check country/tax type if changed create new tax with provided detail
        #     #otherwise update REIT/TaxRate
        return Response(request.data)





