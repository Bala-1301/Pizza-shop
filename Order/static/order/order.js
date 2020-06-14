var cart = []
var subTotal = 0

document.addEventListener("DOMContentLoaded", function(){
	var subTotalSpan = document.getElementById("sub-total").firstElementChild
	
	var pizza = document.getElementById("a1")
	var sub = document.getElementById("a2")
	var pasta = document.getElementById("a3")
	var salad = document.getElementById("a4")
	var platter = document.getElementById("a5")
	
	
	pizza.setAttribute("href","#pizza")
	sub.setAttribute("href","#sub")
	pasta.setAttribute("href","#pasta")
	salad.setAttribute("href","#salad")
	platter.setAttribute("href","#platter")

	
	pizzaSizeChanged = (element) => {
		var form = element.parentElement
		var a = element.dataset
		var sizeIndex = element.selectedIndex
		var select = element.nextElementSibling
		var priceTag = element.parentElement.parentElement.nextElementSibling.nextElementSibling
		var index = select.value
		
		var topPrice = Number(select.options[index].dataset.price)
		
		for(var i = 3; i >= 1; i--){
			select.options[i].remove()
		}
		if(element.options[sizeIndex] === "small"){
			select.options[select.options.length] = new Option(`Single : ₹${a.pizzaOts}`, "1")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaOts}`)
			select.options[select.options.length] = new Option(`Double : ₹${a.pizzaTts}`, "2")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaTts}`)
			select.options[select.options.length] = new Option(`Triple : ₹${a.pizzaThts}`, "3")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaThts}`)
		}
		else{
			select.options[select.options.length] = new Option(`Single : ₹${a.pizzaOtl}`, "1")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaOtl}`)
			select.options[select.options.length] = new Option(`Double : ₹${a.pizzaTtl}`, "2")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaTtl}`)
			select.options[select.options.length] = new Option(`Triple : ₹${a.pizzaThtl}`, "3")
			select.options[select.options.length-1].setAttribute("data-price", `${a.pizzaThtl}`)
		
		}
		var basePrice = Number(element.options[sizeIndex].dataset.pizzaPrice)
		priceTag.innerHTML = "₹"+(basePrice+topPrice).toFixed(2)
		select.selectedIndex = index
	}

	toppingChanged = (element) => {
		var form = element.parentElement
		var childCount = form.childElementCount
		var size = element.previousElementSibling
		var sizeIndex = size.selectedIndex
		var basePrice = Number(size.options[sizeIndex].dataset.pizzaPrice)
		var priceTag = element.parentElement.parentElement.nextElementSibling.nextElementSibling

		var index = element.selectedIndex
		var topPrice = Number(element.options[index].dataset.price)
		
		priceTag.innerHTML = "₹"+(basePrice+topPrice).toFixed(2)
		var select1 = element.nextElementSibling
		var select2 = select1.nextElementSibling
		var select3 = select2.nextElementSibling
		var select = [select1, select2, select3]
		for( var i = 0; i < childCount-2; i++){
			select[i].style.display = "none"
		}
		if (element.selectedIndex < 1){
			return
		}
		var value = element.value
		for(var i = 0; i < value; i++){
			select[i].style = "display: block; display: inline-flex"
		}
	}

	var formSize = document.getElementsByClassName("select")
	for(var i = 0; i < formSize.length; i++){
		formSize[i].onchange = function(){
			var priceTag = this.parentElement.parentElement.nextElementSibling.nextElementSibling
			
			var index = this.selectedIndex
			var price = this.options[index].dataset.price
			priceTag.innerHTML = "₹" + price
		}
	}

	var button = document.getElementsByClassName("button1")
	for(var i = 0; i < button.length; i++){
		button[i].onclick = function(){
			var ul = document.getElementById("cart-ul")
			document.getElementById("cart-p").style.display = "none";
			document.getElementById("proceed-div").style.display = "block";
			var li1 = this.parentElement.parentElement
			var div1 = li1.firstElementChild
			
			var imgDiv1 = div1.firstElementChild
			var img1 = imgDiv1.firstElementChild
			var txtDiv1 = imgDiv1.nextElementSibling
			var itemName1 = txtDiv1.firstElementChild
			
			
			var li2 = li1.cloneNode(true)
			var div2 = li2.firstElementChild
			var imgDiv2 = div2.firstElementChild
			var img2 = imgDiv2.firstElementChild
			var txtDiv2 = imgDiv2.nextElementSibling
			var itemName2 = txtDiv2.firstElementChild
			
			var button = txtDiv2.nextElementSibling
			var price = button.nextElementSibling
			try{
				var form1 = itemName1.nextElementSibling
				var sizeSelect1 = form1.firstElementChild
				var form2 = itemName2.nextElementSibling
				var sizeSelect2 = form2.firstElementChild
				form2.className = "cart-form"
				txtDiv2.removeChild(form2)
			}catch(err){}

			div2.className = "cart-div"
			img2.className = "cart-img"
			itemName2.className = "cart-p"
			
			button.className = "cart-button"
			imgDiv2.className="col-sm-4"
			txtDiv2.className ="col-sm-8 cart-txt-div"
			price.className = "cart-price"

			
			div2.classList.remove("div1")
			li2.classList.remove("col-sm-4")
			li2.classList.remove("text-center")
			
			button.classList.remove("button1")
			price.classList.remove("p2")
			var choice = document.createElement("p")
			try {
				itemName2.firstElementChild.nextElementSibling.remove()
			}
			catch(err){}
			try{
				
				if(sizeSelect2.tagName == "SPAN"){
					throw err
				}
				sizeSelValue = sizeSelect1.value
				console.log(sizeSelValue)
				sizeSelValue = sizeSelValue[0].toUpperCase() + sizeSelValue.slice(1);
				var temp = sizeSelValue
			
				var topping1 = sizeSelect1.nextElementSibling
			
				var top11 = topping1.nextElementSibling
				temp += " | " + top11.value
				
				var top12 = top11.nextElementSibling
				temp += " | " + top12.value
				
				var top13 = top12.nextElementSibling
				temp += " | " + top13.value
				
			}
			catch(err){}
			if(temp)
				choice.innerHTML = temp
			choice.className = "cart-choice"
			txtDiv2.appendChild(choice)
			var hr = document.createElement("hr")
			li2.appendChild(hr)
			ul.append(li2)
			item = {"itemName": itemName1.innerHTML, "description": choice.innerHTML, "price": price.innerHTML.slice(1)}
			cart.push(item)
			subTotal += Number(price.innerHTML.slice(1))
			subTotalSpan.innerHTML = "₹"+subTotal
			
		}
			
	}
});