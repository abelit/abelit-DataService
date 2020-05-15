from flask import Blueprint,jsonify,request
from flask_apscheduler import APScheduler

schedulerbpt = Blueprint('schedulerbpt',__name__)
scheduler = APScheduler()

@schedulerbpt.route('/pause/<string:id>/')
def pause_task(id):
    #暂停
    try:
        scheduler.pause_job(id)
        msg, code = "ok", 200
    except Exception:
        msg, code = "failed to pause job!", 5001

    return jsonify({
        "msg": msg,
        "code": code
    })
    
@schedulerbpt.route('/resume/<string:id>/')
def resume_task(id):
    #恢复
    try:
        scheduler.resume_job(id)
        msg, code = "ok", 200
    except Exception:
        msg, code = "failed to resume job!", 5001

    return jsonify({
        "msg": msg,
        "code": code
    })

@schedulerbpt.route('/get')
def  get_task():
    #获取
    jobs=scheduler.get_jobs()

    import datetime

    result = []
    
    if jobs is not None:
        for job in jobs:
            result.append({
                "job_id": job.id,
                "job_name": job.name,
                "job_task": job.func_ref,
                "job_trigger": str(job.trigger),
                "job_status": "running" if job.next_run_time else "not running"
            })

    print(result)
    return jsonify(result)

@schedulerbpt.route('/delete/<string:id>/')
def remove_task(id):
    #移除
    try:
        scheduler.delete_job(id)
        msg, code = "ok", 200
    except Exception:
        msg, code = "failed to delete job!", 5001

    return jsonify({
        "msg": msg,
        "code": code
    })

@schedulerbpt.route('/add')
def add_task():
    # http://10.46.101.180:5060/api/scheduler/add?id=1002&seconds=10&name=考勤数据同步
    id = request.args.get('id',default='1001',type=str)
    seconds = request.args.get('seconds',default=5,type=int)
    name = request.args.get('name', default='考勤数据同步',type=str)

    try:
        scheduler.add_job(func=sync_data, id=id, args=(request.url_root,id), name=name, trigger='interval', seconds=seconds, replace_existing=False)
        msg, code = "ok", 200
    except Exception as err:
        print(err)
        msg, code = "failed to create job!", 5001

    return jsonify({
        "msg": msg,
        "code": code
    })

def sync_data(url,jobid):
    import urllib.request
    # print(url+'api/employee/syncdata')
    scheduler.pause_job(jobid)
    try:
        urllib.request.urlopen(url+'api/employee/syncdata')
    except Exception:
        pass
    scheduler.resume_job(jobid)
        
    
    