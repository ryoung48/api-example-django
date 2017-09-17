import axios from 'axios'
import Cookie from 'js-cookie'

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

const host = 'http://localhost:8000/'

const doctors = () => {
    return axios.get(`${host}doctors`).then((result) => {
        return result.data
    })
}

const csrfExchange = () => {
    return (!Cookie.get('csrftoken')) ? axios.get(`${host}get-token/`).then((result) => {
        console.log(result.data.token)
        Cookie.set('csrftoken', result.data.token)
    }) : new Promise(function(resolve, reject) {
        resolve(Cookie.get('csrftoken'))
     })
}

const verifyAppointment = (params) => {
    return csrfExchange().then(() => {
        return axios({
            method: 'post',
            url: `${host}appointment/verify/`,
            data: params,
            headers: {
                'X-CSRFToken': Cookie.get('csrftoken')
            }
        }).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

const finalizeCheckin = (params) => {
    return csrfExchange().then(() => {
        return axios({
            method: 'post',
            url: `${host}appointment/finalize/`,
            data: params,
            headers: {
                'X-CSRFToken': Cookie.get('csrftoken')
            }
        }).then((result) => {
            return result.data
        }).catch((error) => {
            console.log(error)
        })
    })
}

export default {
    doctors,
    verifyAppointment,
    finalizeCheckin,
    host
}

