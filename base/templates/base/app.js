
import jsonConfig from './base/assets/class.json' assert {type:"json"};
console.log(jsonConfig);

async function loadJson(){
  const {default:jsonConfig2}= await import('./assets/class.json',{
    assert:{
        type:"json"
    }
  });
  console.log(jsonConfig2);
}

loadJson();