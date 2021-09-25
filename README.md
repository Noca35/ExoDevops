<h1 align="center">ExoDevops</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
</p>

Exercice Devops dont le but est d'écrire un operateur kubernetes minimaliste

> Objectif de l'operateur :
>		* Definir une Custom Ressource Mall qui correspond à un centre commercial qui contient N boutiques et l'item vendu par ce boutiques.
>		* L'operateur va dimensionner le nombre de pod qui correspond aux N boutiques et definir l'item vendu basé sur les valeurs de la custom ressource 

## Installation de l'environnement

> Près requis :
>	* Hyperviseur
>	* Kubectl
>	* Minikube
>	* Framework python kopf	

guide d'installation :

https://kubernetes.io/fr/docs/tasks/tools/install-minikube/


## Test du déploiement

```sh
minikube start
minikube dashboard
```

A ce stade le dashboard kubernetes devrait apparaitre à l'écran

## Usage

1.Dans notre cas l'opérateur va être déployer dans le cluster, on va devoir donc lui attribuer les droits nécéssaire à son bon fonctionnement

```sh
kubectl apply -f crd.yaml ## definition de la custom ressource
kubectl apply -f role-operator.yaml ## definition des rôles de l'operateur
kubectl apply -f rol_bind-operator.yaml ## application des rôles à l'operateur 
```
2.Deploiement de l'operateur dans le cluster

```sh
kubectl apply -f operator-deployment.yaml
```

3.Definition des ressources de la galerie marchande

```sh
kubectl apply -f mall.yaml
```




```sh
test
```

## Author

👤 **Noca35**

* Github: [@Noca35](https://github.com/Noca35)

