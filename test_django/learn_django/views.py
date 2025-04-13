from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
# Create your views here.
# 写业务逻辑
# require_http_methods 代表调用请求时请求方法必须为GET请求
@require_http_methods(['GET'])
def all_stu_info(request):
    '''
    查询所有学员的信息
    @params age 性別
    @return code 0 信息获取成功 1信息获取失败
    @return msg 返回所有学员的信息 学员信息不存在
    '''
    response={}
    response['code'] = 0
    response['msg']='返回所有学员的信息'
    return JsonResponse(response)  
  # try:
    #     # 从数据库获取所有学生，按创建时间倒序排列
    #     students = student.objects.all().order_by('-create_time').values(
    #         'id', 
    #         'name', 
    #         'age', 
    #         'phone', 
    #         'create_time'
    #     )
        
    #     # 格式化日期时间
    #     student_list = []
    #     for stu in students:
    #         student_data = dict(stu)
    #         student_data['create_time'] = stu['create_time'].strftime('%Y-%m-%d %H:%M:%S')
    #         student_list.append(student_data)
        
    #     return JsonResponse({
    #         'code': 0,
    #         'msg': '学员信息获取成功',
    #         'data': student_list
    #     })
    
    # except Exception as e:
    #     return JsonResponse({
    #         'code': 1,
    #         'msg': f'学员信息获取失败: {str(e)}',
    #         'data': []
    #     }, status=500)