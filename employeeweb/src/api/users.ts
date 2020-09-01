import request from '@/utils/request'

export const getUsers = (params: any) =>
  request({
    url: '/employee/users',
    method: 'get',
    params
  })

export const getUserInfo = (data: any) =>
  request({
    url: '/employee/users/info',
    method: 'post',
    data
  })

export const getUserByName = (username: string) =>
  request({
    url: `/employee/users/${username}`,
    method: 'get'
  })

export const updateUser = (username: string, data: any) =>
  request({
    url: `/employee/users/${username}`,
    method: 'put',
    data
  })

export const deleteUser = (username: string) =>
  request({
    url: `/employee/users/${username}`,
    method: 'delete'
  })

export const login = (data: any) =>
  request({
    url: '/employee/users/login',
    method: 'post',
    data
  })

export const logout = () =>
  request({
    url: '/employee/users/logout',
    method: 'post'
  })

export const register = (data: any) =>
  request({
    url: '/employee/users/register',
    method: 'post',
    data
  })
