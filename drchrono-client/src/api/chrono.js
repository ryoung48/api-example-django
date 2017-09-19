import axios from 'axios'
import Cookie from 'js-cookie'

const host = 'http://localhost:8000/'

const login = host + 'login/drchrono/'

axios.defaults.withCredentials = true

const loggedIn = () => {
    return axios.get(`${host}auth-check/`).then((result) => {
        return result.data.user !== 'AnonymousUser'
    })
}

const buildPost = (params, endpoint) => {
    return {
        method: 'post',
        url: host + endpoint,
        data: params,
        headers: {
            'X-CSRFToken': Cookie.get('csrftoken')
        }
    }
}

const doctors = () => {
    return axios.get(`${host}doctors`).then((result) => {
        return result.data
    })
}

const csrfExchange = () => {
    return (!Cookie.get('csrftoken')) ? axios.get(`${host}get-token/`).then((result) => {
        Cookie.set('csrftoken', result.data.token)
    }) : new Promise(function(resolve, reject) {
        resolve(Cookie.get('csrftoken'))
     })
}

const verifyAppointment = (params) => {
    return csrfExchange().then(() => {
        return axios(buildPost(params, 'appointment/verify/')).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

const getAppointments = (id) => {
    return axios.get(`${host}appointment/${id}/`).then((result) => {
        return result.data
    })
}

const visit = (params) => {
    return csrfExchange().then(() => {
        return axios(buildPost(params, 'appointment/visit/')).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

const updateDoctorStatus = (params) => {
    return csrfExchange().then(() => {
        return axios(buildPost(params, 'doctor/status/')).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

const finalizeCheckin = (params) => {
    return csrfExchange().then(() => {
        return axios(buildPost(params, 'appointment/finalize/')).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

export default {
    doctors,
    verifyAppointment,
    getAppointments,
    finalizeCheckin,
    updateDoctorStatus,
    loggedIn,
    visit,
    host,
    login
}

