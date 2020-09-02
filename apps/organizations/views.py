from django.shortcuts import render
from django.views.generic.base import View

from apps.organizations.models import CourseOrg, City
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        # 通过机构类别筛选课程机构
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过城市筛选课程机构
        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))
        org_nums = all_orgs.count()

        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by('-students')
        if sort == 'courses':
            all_orgs = all_orgs.order_by('-course_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对课程机构数据进行分页
        p = Paginator(all_orgs, per_page=10, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'all_orgs': orgs, 'org_nums': org_nums, 'all_citys': all_citys, 'category': category,
            'city_id': city_id, 'sort': sort, 'hot_orgs': hot_orgs
        })
