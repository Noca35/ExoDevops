<h1 align="center">ExoDevops</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
</p>

Exercice Devops dont le but est d'écrire un operateur kubernetes minimaliste

> L'objectif de l'opérateur est de definir une Custom Ressource Mall qui correspond à un centre commercial qui contient N boutiques et l'item vendu par ces boutiques.
> Grâce à ces données, l'operateur va dimensionner le nombre de pod qui correspond aux N boutiques et definir l'item vendu basé sur les valeurs de la custom ressource.
> Les informations sur le nom de la boutique ainsi que l'objet vendu seront affiché chaques secondes dans les différents pod de la boutique. 

## Installation de l'environnement

> Près requis :
>	* Hyperviseur
>	* Kubectl
>	* Minikube
>	* Framework python kopf	

guide d'installation du cluster :

https://kubernetes.io/fr/docs/tasks/tools/install-minikube/

## Test du déploiement

```sh
minikube start
minikube status
```

## Usage

1.Dans notre cas l'opérateur va être déployé dans le cluster, on va devoir donc lui attribuer les droits nécéssaire à son bon fonctionnement

```sh
kubectl apply -f crd.yaml ## definition de la custom ressource
kubectl apply -f role-operator.yaml ## definition des rôles de l'operateur
kubectl apply -f role_bind-operator.yaml ## application des rôles à l'operateur 
```
2.Deploiement de l'operateur dans le cluster

```sh
kubectl apply -f operator-deployment.yaml
```

3.Definition des ressources de la galerie marchande

```sh
kubectl apply -f mall.yaml
```

4.Confirmation de la création des ressources

A ce stade une configmap "mall-config" a du être créée avec l'item "socks" ainsi que 10 pods shop basé sur la custom ressource mall.yaml :

```yaml
apiVersion: mall.my.domain/v1
kind: Mall
metadata:
  name: mall-first
spec:
  replicas: 5
  item: socks
```

replicas correspondant au nombre de boutique dans la gallerie marchande et item l'objet vendu

5.Affichage du message d'information

Commençons par lister les pods déployés et verifions que la configmap contient la bonne variable 

```sh
kubectl get pods --all-namespaces
kubectl describe configmaps mall-config
```

Et ensuite affichons les logs d'un pod shop au choix en remplaçant my-pod par un des pods shop listé

```sh
kubectl logs -f my-pod
```

Le message retournant le nom du shop ainsi que l'objet vendu devrait apparaître

6.scalabilité des shop

Modifions la ressource malls.yaml :

```yaml
apiVersion: mall.my.domain/v1
kind: Mall
metadata:
  name: mall-first
spec:
  replicas: 3
  item: apple
```

Appliquons la :

```sh
kubectl apply -f mall.yaml
```

Verifions le nombre de pods déployés ainsi que les données de la configmap on bien changé dynamiquement:

```sh
kubectl get pods --all-namespaces
kubectl describe configmaps mall-config

```
Le nombre de pods shop devraient descendre à 5 et le la variable de la configmap env.item = apple


7.Test de suppression de la ressource mall.yaml

```sh
kubectl delete -f mall.yaml
```

Avec cette commande on observe que les pods shop on été supprimé ainsi que la configmap "mall-config"


## Rollout restart des pods quand la configmap est update

J'ai commencé à creuser le sujet à ce niveau, je n'ais pas trouvé de solutions simple 

ressource : https://github.com/stakater/Reloader


## Author

👤 **Noca35**

