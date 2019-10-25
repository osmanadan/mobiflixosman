module.exports = {
  apps : [{
    name: 'mobiflix',
    script: 'npm',

    // Options reference: https://pm2.io/doc/en/runtime/reference/ecosystem-file/
    args: 'run start:production',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }],

  deploy : {
    production : {
    },staging:{
     user:'denisshockwave',
     host : 'mobiflix.tv',
     ref: 'origin/develop',
     repo: 'git@github.com:denisshockwave/mobiflix.git',
     path:'',
     key:'',
     ssh_options:['ForwardAgent=yes'],
    'post_deploy':'npm install && pm2 reload ecosystem.config.js --env production'
},
dev:{}
  }
};
