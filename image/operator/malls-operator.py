import kopf
import pykube
import yaml

@kopf.on.create('mall.my.domain', 'v1', 'malls')
def create_1(spec, **kwargs):
    doc = create_deployment(spec)
    doc1 = create_configmap(spec)
    kopf.adopt(doc)
    kopf.adopt(doc1)

    api = pykube.HTTPClient(pykube.KubeConfig.from_env())
    deployment = pykube.Deployment(api, doc)
    deployment.create()

    configmap = pykube.ConfigMap(api, doc1)
    configmap.create()

    api.session.close()

@kopf.on.update('mall.my.domain', 'v1', 'malls')
def update_1(spec, **kwargs):
    api = pykube.HTTPClient(pykube.KubeConfig.from_env())
    deployment = pykube.Deployment.objects(api).get(name="shop")
    deployment.replicas = spec.get('replicas', 1)
    deployment.update()

    doc1 = create_configmap(spec)
    pykube.ConfigMap(api, doc1).update()

    api.session.close()

def create_deployment(spec):
    return yaml.safe_load(f"""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: shop
        spec:
          replicas: {spec.get('replicas', 1)}
          selector:
            matchLabels:
              app: mall
          template:
            metadata:
              labels:
                app: mall
            spec:
              containers:
                - name: shop
                  image: noca/shop
                  env:
                    - name: STORE_ITEM_KEY
                      valueFrom:
                        configMapKeyRef:
                          name: mall-config
                          key: env.item
    """)

def create_configmap(spec):
    return yaml.safe_load(f"""
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: mall-config
          namespace: default
          annotations:
            configmap/update: 'yes'
        data:
         env.item: {spec.get('item')}
    """)
